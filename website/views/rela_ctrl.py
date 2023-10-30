from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from database import get_user_database
from baiduspider import BaiduSpider

rela_ctrl = Blueprint('rela_ctrl', __name__)


@rela_ctrl.route('/rela_results')
def rela_results():
    query = request.args.get('str')
    print(query)
    spider = BaiduSpider(
            cookie='BIDUPSID=317B79995A3443BEE218809A98B17862; PSTM=1670302796; BAIDUID=317B79995A3443BE3185450DC86FA5CC:FG=1; BD_UPN=12314753; BDUSS=GRWVnNQRGV3VllQMjFqMjBiVjhZeWRNTzJkbVhPLVF5MkNsM250SjE3a25Ld05sRVFBQUFBJCQAAAAAAAAAAAEAAAB3N9OkuerL2bXEyPH2qQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACee22QnnttkU; BDUSS_BFESS=GRWVnNQRGV3VllQMjFqMjBiVjhZeWRNTzJkbVhPLVF5MkNsM250SjE3a25Ld05sRVFBQUFBJCQAAAAAAAAAAAEAAAB3N9OkuerL2bXEyPH2qQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACee22QnnttkU; H_WISE_SIDS=131862_132548_216851_213359_214801_110085_244712_254833_261717_236312_256419_265881_266359_265986_265615_256303_259033_268592_268707_268030_259642_256151_269730_269832_269904_269770_267066_256739_270460_264424_270547_270922_271034_271023_271169_271175_257179_271227_267659_269296_271323_265034_265825_266027_271581_270102_271562_271877_271813_269876_271949_271943_234296_234208_179346_272223_272278_266565_267596_272365_272012_272336_272460_253022_272078_271689_272764_272815_272838_272802_260335_271285_273058_267559_273091_273121_273147_273176_273263_273245_273300_273400_273392_271157_270055_273475_273464_273528_273521_273515_270179_273603_271147_273673_273703_264170_270186_272264_273807_273734_263619_273898_273164_273922_274081_273931_273966_274140_273847_269610_274206_274237_273789_273044_273595_272693_274300_272855_203519_274356_272319_8000056_8000111_8000134_8000136_8000149_8000153_8000163_8000175_8000181_8000186_8000204; H_WISE_SIDS_BFESS=131862_132548_216851_213359_214801_110085_244712_254833_261717_236312_256419_265881_266359_265986_265615_256303_259033_268592_268707_268030_259642_256151_269730_269832_269904_269770_267066_256739_270460_264424_270547_270922_271034_271023_271169_271175_257179_271227_267659_269296_271323_265034_265825_266027_271581_270102_271562_271877_271813_269876_271949_271943_234296_234208_179346_272223_272278_266565_267596_272365_272012_272336_272460_253022_272078_271689_272764_272815_272838_272802_260335_271285_273058_267559_273091_273121_273147_273176_273263_273245_273300_273400_273392_271157_270055_273475_273464_273528_273521_273515_270179_273603_271147_273673_273703_264170_270186_272264_273807_273734_263619_273898_273164_273922_274081_273931_273966_274140_273847_269610_274206_274237_273789_273044_273595_272693_274300_272855_203519_274356_272319_8000056_8000111_8000134_8000136_8000149_8000153_8000163_8000175_8000181_8000186_8000204; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BDSFRCVID=eR0OJeC626f-uY6qKvS6hFXv6eK80xnTH6aoGogJrEZySEMZz5I7EG0PXx8g0KuMMWnQogKK0mOTHv-F_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF=tR4HoDKbtK-3fP36q4uMq4tHePcCJURZ5mAqoJRe2-JTfRQX3xOCMMKR2lQiJj3rKH6naIQDthT1VbjGDR6iD4DjeJohJxc43bRTQpCy5KJvfj6Dybu5hP-UyN3LWh37btjlMKoaMp78jR093JO4y4Ldj4oxJpOJ5JbMonLafDD5bKDwDT835PLHMp_X5to05TIX3b7EfKOtsl7_bf--DR-FLpQO2JoG-bnnKln2yR7lbKb-5pQxy5K_hp-DBlRvfCjRoM7E5hO2ep5HQT3m2JvbbN3i0DrgteJBWb3cWKJV8UbS5RrM34LFXfnK5qLOXKQ8aJKKJj6jObRmb67JD-50eGKfqTKJJnIDV-b-KROqKCKlM4nDq4tehHRJQMo9WDTm_DoEaj60sPolLRoTKPkzWMOOBTb23nPe-pPKKR7lOMcYhxrTM--hKMuf-lOk3mkjbpnGfn02OP5P35oVQ44syP4j2xRnWTFLKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJzJCFKMIPCj58hDjP3KxQ2KCCttCQy3jrJabC3oJ6JXU6qLT5XhfILhfbH-mrtbxnS3fnfJhP6-U8MDp0njxQyLxvz2CoA5bnjMtJEMP5MWfonDh8n3H7MJUntKHPtWlQO5hvvhb6O3M7-qfKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_EtT_HJJCD_KtQb-3bKR5gK4QbKP4E52T22jn-LJR9aJ5nJD_-e66GWjjaynK9jx7lXnKq5m0OoPn8QpP-HJ7jhPJkKxLl2Jb4WlTEJmKfKl0MLUnWbb0xynoYXq-H0fnMBMPjamOnaPLE3fAKftnOM46JehL3346-35543bRTLnLy5KJtMDcnK4-XD6O3DajP; BDSFRCVID_BFESS=eR0OJeC626f-uY6qKvS6hFXv6eK80xnTH6aoGogJrEZySEMZz5I7EG0PXx8g0KuMMWnQogKK0mOTHv-F_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tR4HoDKbtK-3fP36q4uMq4tHePcCJURZ5mAqoJRe2-JTfRQX3xOCMMKR2lQiJj3rKH6naIQDthT1VbjGDR6iD4DjeJohJxc43bRTQpCy5KJvfj6Dybu5hP-UyN3LWh37btjlMKoaMp78jR093JO4y4Ldj4oxJpOJ5JbMonLafDD5bKDwDT835PLHMp_X5to05TIX3b7EfKOtsl7_bf--DR-FLpQO2JoG-bnnKln2yR7lbKb-5pQxy5K_hp-DBlRvfCjRoM7E5hO2ep5HQT3m2JvbbN3i0DrgteJBWb3cWKJV8UbS5RrM34LFXfnK5qLOXKQ8aJKKJj6jObRmb67JD-50eGKfqTKJJnIDV-b-KROqKCKlM4nDq4tehHRJQMo9WDTm_DoEaj60sPolLRoTKPkzWMOOBTb23nPe-pPKKR7lOMcYhxrTM--hKMuf-lOk3mkjbpnGfn02OP5P35oVQ44syP4j2xRnWTFLKfA-b4ncjRcTehoM3xI8LNj405OTbIFO0KJzJCFKMIPCj58hDjP3KxQ2KCCttCQy3jrJabC3oJ6JXU6qLT5XhfILhfbH-mrtbxnS3fnfJhP6-U8MDp0njxQyLxvz2CoA5bnjMtJEMP5MWfonDh8n3H7MJUntKHPtWlQO5hvvhb6O3M7-qfKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_EtT_HJJCD_KtQb-3bKR5gK4QbKP4E52T22jn-LJR9aJ5nJD_-e66GWjjaynK9jx7lXnKq5m0OoPn8QpP-HJ7jhPJkKxLl2Jb4WlTEJmKfKl0MLUnWbb0xynoYXq-H0fnMBMPjamOnaPLE3fAKftnOM46JehL3346-35543bRTLnLy5KJtMDcnK4-XD6O3DajP; H_PS_PSSID=39313_39365_39396_39411_39435_39480_39373_39466_39234_39405_39486_26350_39421; BA_HECTOR=0004042l20810h81010k058i1iial3v1p; ZFY=:Bt8eoJ1E25S0MQPrBYje6ogpdPmG:AbKAewTZr9YBIrk:C; BAIDUID_BFESS=317B79995A3443BE3185450DC86FA5CC:FG=1; channel=baidusearch; RT="z=1&dm=baidu.com&si=4cfea510-6da9-4334-a3a9-41608b1a1f11&ss=lnkdf20d&sl=h&tt=72w&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=45v4&ul=49yy&hd=49z9"; delPer=0; BD_CK_SAM=1; PSINO=2; B64_BOT=1; COOKIE_SESSION=191_3_0_0_8_0_1_0_0_0_0_0_106_0_12_0_1696945781_1696832671_1696945769%7C4%230_1_1696832671%7C1; baikeVisitId=8c8f916a-f6a5-47ce-b1e9-feece5e82c2a; H_PS_645EC=8c68LzKt9euTSRWlGKjBiZfIZNJRu%2BHrvcZZTv8%2Bqzewhjp8yhHwY%2FNAvuo; WWW_ST=1696945997326')
    result = BaiduSpider().search_web(query=query, pn=5).plain
    d = dict()
    dr = dict()
    for i in range(1, len(result)):
        d[i] = result[i]
    for j in range(len(result[0]["results"])):
        dr[j] = result[0]["results"][j]
    return render_template('web_search_results.html', dic=d, relate=dr)
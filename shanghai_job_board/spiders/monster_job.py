import scrapy
import json
import psycopg2
from psycopg2.extensions import AsIs
from collections import OrderedDict

conn = psycopg2.connect(
  dbname='jobs',
  user='enterwizard'
)
cur = conn.cursor()

class MonsterJobs(scrapy.Spider):
  name = 'monster'
  allowed_domains = ['www.monster.com.hk']
  start_urls = ['https://www.monster.com.hk/middleware/jobsearch?sort=2&limit=5&locations=Shanghai']

  def parse(self, response):
    results = json.loads(response.text)
    resultsTrimmed = results["jobSearchResponse"]["data"]
    resultsFiltered = [i for i in resultsTrimmed if "index" not in i]
    print(resultsFiltered, 'i am resultsFiltered')

    # popItems = ["id", "jobId", "kiwiJobId", "kiwiCompanyId", "kiwiRecruiterId", "recruiterId", "companyId", "walkInVenue", "referenceCode", "status", "accountId", "hideCompanyName", "autoMatch", "showContactDetails", "graceJob", "quickJob", "channelId", "channelName", "isBold", "isJdLogo", "isSearchLogo", "isCJT", "isMicrosite", "redirectStage", "isApplied", "isSaved", "order", "questionnaire", "minimumExperience", "maximumExperience", "minimumSalary", "maximumSalary", "functions", "seoCompanyUrl", "seoJdUrl"]

    popItems = ["id", "jobId", "kiwiJobId", "kiwiCompanyId", "kiwiRecruiterId", "recruiterId", "companyId", "walkInVenue", "referenceCode", "status", "accountId", "hideCompanyName", "autoMatch", "showContactDetails", "graceJob", "quickJob", "channelId", "channelName", "isBold", "isJdLogo", "isSearchLogo", "isCJT", "isMicrosite", "redirectStage", "isApplied", "isSaved", "order", "questionnaire", "minimumExperience", "maximumExperience", "minimumSalary", "maximumSalary", "functions", "seoCompanyUrl", "roles" "seoJdUrl", "createdAt", "freshness", "closedAt", "updatedAt"]

    groupJobs = []
    for index, individualJob in enumerate(resultsFiltered):
      try:
        [individualJob.pop(key) for key in popItems]
        print(individualJob, ' i am individualJob')
        individualJobValues = OrderedDict(individualJob).values()
        print(individualJobValues, 'i am individualJobValues')
        # individualJobValuesList = list(individualJobValues)
        # groupJobs.append(individualJobValuesList)
      except KeyError:
        pass

    # print(groupJobs, 'i am group jobs')
    # for index, eachJob in enumerate(groupJobs):
    #   cur.execute("INSERT INTO monster_test (redirecturl, title, locations, industries, summary, jobtypes, employmenttypes, minimumexperiencefilter, maximumexperiencefilter, employertypes, companyname, applyurl, recruitercontactnumber, jobsource, postingboard, isocode, recruitername, companyprofile, sitecontext, activejob, totalapplicants, exp, salary, postedby, isfresh, ishotjob, isselected, isprofilecomplete) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(eachJob[0],eachJob[1],eachJob[2],eachJob[3],eachJob[4],eachJob[5],eachJob[6],eachJob[7],eachJob[8],eachJob[9],eachJob[10],eachJob[11],eachJob[12],eachJob[13],eachJob[14],eachJob[15],eachJob[16],eachJob[17],eachJob[18],eachJob[19],eachJob[20],eachJob[21],eachJob[22],eachJob[23],eachJob[24],eachJob[25],eachJob[26],eachJob[27]))

    # conn.commit()
    # cur.close()
    # conn.close()
    # print(len(individualJobValuesList), 'dolzina')

      # REAL ONE WITH MORE ATTRIBUTES
      # cur.execute("INSERT INTO monster_jobs (redirecturl, title, locations, createdat, updatedat, industries, summary, jobtypes, employmenttypes, minimumexperiencefilter, maximumexperiencefilter, employertypes, companyname, applyurl, recruitercontactnumber, jobsource, postingboard, isocode, recruitername, companyprofile, sitecontext, freshness, closedat, activejob, totalapplicants, exp, salary, postedby, isfresh, ishotjob, isselected, isprofilecomplete) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, %s)",(individualJobValuesList[0],individualJobValuesList[1],individualJobValuesList[2],individualJobValuesList[3],individualJobValuesList[4],individualJobValuesList[5],individualJobValuesList[6],individualJobValuesList[7],individualJobValuesList[8],individualJobValuesList[9],individualJobValuesList[10],individualJobValuesList[11],individualJobValuesList[12],individualJobValuesList[13],individualJobValuesList[14],individualJobValuesList[15],individualJobValuesList[16],individualJobValuesList[17],individualJobValuesList[18],individualJobValuesList[19],individualJobValuesList[20],individualJobValuesList[21],individualJobValuesList[22],individualJobValuesList[23],individualJobValuesList[24],individualJobValuesList[25],individualJobValuesList[26],individualJobValuesList[27],individualJobValuesList[28],individualJobValuesList[29],individualJobValuesList[30], individualJobValuesList[31]))

  # conn.commit()
  # cur.close()
  # conn.close()
  # testing = ['moo', 22]
  # cur.execute("INSERT INTO test6 (property1, property2) VALUES (%s, %s)",(testing[0], testing[1]))

    # print(resultsFiltered)


# Crunshbase_Scraper
A Software that scrapes companies' data from Crunshbase and stores Data in MongoDB

#### input: list of companies' names

#### example of data extracted (company: Instadeep)

````[{
	"_id": {
		"$oid": "60a648d679c1ebfe3bbe0bc0"
	},
	"about_description": "InstaDeep delivers AI-powered decision-making systems for the Enterprise, to solve some of the world’s most complex industrial problems.",
	"detail_description": "Founded in 2014, InstaDeep is an EMEA leader in decision-making AI products for the Enterprise, with headquarters in London, and offices in Paris, Tunis, Lagos, Dubai and Cape Town. With expertise in both machine intelligence research and concrete business deployments, the Company provides a competitive advantage to its partners in an AI-first",
	"description_list": [
		"London, England, United Kingdom",
		"101-250",
		"Series A",
		"Private",
		"www.instadeep.com/",
		"7,251"
	],
	"industries": "Artificial Intelligence",
	"founded_date": "Oct 8, 2015",
	"founders": "Karim Beguir, Zohra Slim",
	"operating_status": "Active",
	"last_funding_type": "Series A",
	"legal_name": "InstaDeep Ltd",
	"company_type": "For Profit",
	"contact_email": "hello@instadeep.com",
	"phone_number": "+44 207 193 6553",
	"technology_info": {
		"description": "InstaDeep Ltd is actively using 44 technologies for its website, according to BuiltWith. These include Viewport Meta, IPhone / Mobile Compatible, and SPF.",
		"active_tech_count": "44",
		"monthly_visits": "3,096",
		"monthly_visits_growth": "270.78%"
	},
	"activity": [{
			"type": "News",
			"date": "Apr 23, 2021",
			"source": "The Innovator —",
			"name": "Startup Of The Week: InstaDeep",
			"link": "https://theinnovator.news/startup-of-the-week-instadeep/"
		},
		{
			"type": "News",
			"date": "Feb 19, 2021",
			"source": "Medium —",
			"name": "#SGGlobal21 Startup Program: Accelerate Startups Announced!",
			"link": "https://link.medium.com/yIlUtbV8Ydb"
		},
		{
			"type": "News",
			"date": "Jan 27, 2021",
			"source": "AiThority —",
			"name": "Kao Data to Host InstaDeep’s HPC and AI Supercomputer, Expanding R&D Capabilities",
			"link": "https://aithority.com/data-center-and-co-location/kao-data-to-host-instadeeps-hpc-and-ai-supercomputer-expanding-rd-capabilities/"
		},
		{
			"type": "News",
			"date": "Jan 26, 2021",
			"source": "ComputerWeekly.com —",
			"name": "Kao Data signs AI-focused life sciences startup InstaDeep as a customer",
			"link": "https://bit.ly/3a69cwT"
		},
		{
			"type": "News",
			"date": "Nov 25, 2020",
			"source": "GlobeNewswire News Room —",
			"name": "BioNTech and InstaDeep Announce Strategic Collaboration and Form AI Innovation Lab to Develop Novel Immunotherapies",
			"link": "https://bit.ly/39jljbg"
		},
		{
			"type": "News",
			"date": "Nov 25, 2020",
			"source": "GlobeNewswire News Room —",
			"name": "BioNTech and InstaDeep Announce Strategic Collaboration and Form AI Innovation Lab to Develop Novel Immunotherapies",
			"link": "https://www.globenewswire.com/news-release/2020/11/25/2133666/0/en/BioNTech-and-InstaDeep-Announce-Strategic-Collaboration-and-Form-AI-Innovation-Lab-to-Develop-Novel-Immunotherapies.html"
		},
		{
			"type": "News",
			"date": "Sep 4, 2019",
			"source": "Ventureburn —",
			"name": "French government announces initiative to fly three SA tech startups to France",
			"link": "https://ventureburn.com/2019/09/french-government-announces-initiative-to-fly-three-sa-tech-startups-to-france/"
		},
		{
			"type": "Funding Round",
			"date": "May 9, 2019",
			"content": "InstaDeep Ltd raised $7,000,000 / Series A from AfricInvest and Endeavor CatalystInstaDeep Ltd"
		},
		{
			"type": "Funding Round",
			"date": "Feb 13, 2019",
			"content": "InstaDeep Ltd raised an undisclosed amount / Non Equity Assistance from Plug and PlayInstaDeep Ltd"
		},
		{
			"type": "Funding Round",
			"date": "Jan 1, 2017",
			"content": "InstaDeep Ltd raised an undisclosed amount / Seed from Adam Sadiq and Malek MeslemaniInstaDeep Ltd"
		}
	],
	"events": [{
			"name": "NVIDIA GTC 2021",
			"role": "Exhibitor",
			"date": "Apr 12, 2021",
			"image": "https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_85,w_85,f_auto,b_white,q_auto:eco/agi2gqa6nx16gypmwloj",
			"link": "https://www.crunchbase.com/event/nvidia-gtc-2019"
		},
		{
			"name": "MWC Barcelona",
			"role": "Exhibitor",
			"date": "Jun 28, 2020",
			"image": "https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_85,w_85,f_auto,b_white,q_auto:eco/cwxsq2uxyyrytixrwmbo",
			"link": "https://www.crunchbase.com/event/mwc-2020-barcelona"
		},
		{
			"name": "GTC 2018",
			"role": "Exhibitor",
			"date": "Mar 26, 2018",
			"image": "https://res.cloudinary.com/crunchbase-production/image/upload/c_lpad,h_85,w_85,f_auto,b_white,q_auto:eco/nks6ffutbhkvvxzjnvxb",
			"link": "https://www.crunchbase.com/event/gtc-2018"
		}
	],
	"team": [{
			"image": "https://res.cloudinary.com/crunchbase-production/image/upload/c_thumb,h_85,w_85,f_auto,g_faces,z_0.7,b_white,q_auto:eco/bvsv32smdhqbpqtpkume",
			"name": "Karim Beguir",
			"profile_link": "https://www.crunchbase.com/person/karim-beguir",
			"role": "Co-Founder & CEO"
		},
		{
			"image": "https://res.cloudinary.com/crunchbase-production/image/upload/c_thumb,h_85,w_85,f_auto,g_faces,z_0.7,b_white,q_auto:eco/dcq13anvphlcdrk3qdij",
			"name": "Zohra Slim",
			"profile_link": "https://www.crunchbase.com/person/zohra-slim",
			"role": "Co-Founder and CD&VO"
		},
		{
			"image": "https://res.cloudinary.com/crunchbase-production/image/upload/c_thumb,h_85,w_85,f_auto,g_faces,z_0.7,b_white,q_auto:eco/vluoqxxswdjudalvgiwt",
			"name": "Isabelle Levard",
			"profile_link": "https://www.crunchbase.com/person/isabelle-levard",
			"role": "Group CFO"
		}
	],
	"funding_rounds_info": {
		"number_of_funding_rounds": "3",
		"total_funding_amount": "$7M",
		"number_of_lead_investors": "1",
		"number_of_investors": "5",
		"rounds": [{
				"announced_date": "May 9, 2019",
				"transaction_name": "Series A - InstaDeep Ltd",
				"transaction_link": "https://www.crunchbase.com/funding_round/instadeep-series-a--53de9b88",
				"investors": "2",
				"money_raised": "$7M",
				"lead_investor": {
					"name": "AfricInvest",
					"link": null
				}
			},
			{
				"announced_date": "Feb 13, 2019",
				"transaction_name": "Non Equity Assistance - InstaDeep Ltd",
				"transaction_link": "https://www.crunchbase.com/funding_round/instadeep-non-equity-assistance--b76eeea7",
				"investors": "1",
				"money_raised": "—",
				"lead_investor": {
					"name": "—",
					"link": null
				}
			},
			{
				"announced_date": "Jan 1, 2017",
				"transaction_name": "Seed Round - InstaDeep Ltd",
				"transaction_link": "https://www.crunchbase.com/funding_round/instadeep-seed--339b0805",
				"investors": "2",
				"money_raised": "—",
				"lead_investor": {
					"name": "—",
					"link": null
				}
			}
		]
	},
	"status": "succeeded"
}]````

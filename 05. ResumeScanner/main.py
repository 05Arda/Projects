import pandas as pd

def scan_resume(resume, criterias):
    score = 0
    for key in criterias:
        cs = criterias[key].replace(' ', '').split(',')
        if key == 'Total_Exp':
            if resume[key] >= int(cs[0]):
                score += 1
        elif len(cs[0]) > 0:
            for c in cs:
                score += 1 if c.lower() in resume[key].lower() else 0
    return score


def getCriterias(data):
    maxScore = 0
    criteria = dict()
    for c in data.columns[3:]:
        pref = input(f'Enter {c} criteria: ')
        maxScore += len(pref.strip().split(',')) if len(pref) > 0 else 0
        criteria[c] = pref
    return criteria, maxScore


def getMinScore(maxScore):
    minScore = -1
    while minScore < 0 or minScore > maxScore:
        minScore = int(input(f'Enter minimum score[0, {maxScore}]: '))
        if minScore < 0 or minScore > maxScore:
            print('Invalid minimum score')
    return minScore



def __main__():
    data = pd.read_csv('resumes.csv')
    data.index = data['Name']

    criteria, maxScore = getCriterias(data)
    minScore = getMinScore(maxScore)

    successfulApplicants = pd.DataFrame(columns=data.columns)

    data = data.to_dict(orient='index')

    for applicant in data:
        if scan_resume(data[applicant], criteria) >= minScore:
            successfulApplicants.loc[len(successfulApplicants)] = data[applicant]

    successfulApplicants.to_csv('successfulApplicants.csv', index=False)
    if len(successfulApplicants) == 0:
        print('No successful applicants found')
    else:
        print('Successful applicants have been saved to successfulApplicants.csv')
    quit()

if __name__ == '__main__':
    __main__()
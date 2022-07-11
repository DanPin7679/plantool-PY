from typing import List
from pydantic import BaseModel
import functools

class Results(BaseModel):
    age: List[float] = []
    salaries: List[float] = []
    contributions: List[float] = []
    

def calc(inputs):
    
    age = list(range(int(inputs.age), int(inputs.end_age)))
    sal_increase = inputs.exp_sal_increase
    exp_contribution_rate = inputs.exp_contribution_rate
    salaries = functools.reduce(accum, sal_increase, [inputs.salary])
    print(len(salaries))
    contributions = ( exp_contribution_rate[i] * salaries[i] for i in range(len(salaries)))

    results = Results(
        age=age,
        salaries=salaries,
        contributions=contributions
    )

    return results


def accum(sal1, increase_rate):
    sal1.append(sal1[-1] * (1+increase_rate))
    return sal1



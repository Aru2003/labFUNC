def resume(name,age, experience):
    if age >=20:
        return f"name:{name}, age:{age}, experience:{experience}"
    else:
        return f"Жасы 20-дан аспаған"
 
name =  "Aruzhan"
age=19
experience=2
print(resume(name,age,experience))

def non_functional_resume(name,age,experience):
    if age >=25:
        print(f"name:{name}, age:{age}, experience:{experience}")
    else:
        print("Жасы 25-тен аспаған")
non_functional_resume(name,age,experience)
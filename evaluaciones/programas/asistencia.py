alumnos = ['Pepito', 'Yayita', 'Fulanita', 'Panchito']
asistencia = [
    [True,  True,  True,  False, False, False, False],
    [True,  True,  True,  False, True,  False, True ],
    [True,  True,  True,  True,  True,  True,  True ],
    [True,  True,  True,  False, True,  True,  True ]]

def total_por_alumno(asistencia):
    r = []
    for l in asistencia:
        s = 0
        for v in l:
            if v:
                s = s + 1
        r.append(s)
    return r

def alumno_estrella(asistencia):
    t = total_por_alumno(asistencia)
    m = max(t)
    i = t.index(m)
    return alumnos[i]

print(total_por_alumno(asistencia))
#print(total_por_clase(asistencia))
print(alumno_estrella(asistencia))




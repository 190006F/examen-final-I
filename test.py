import libreria
assert (libreria.validar_primer_nombre("12")==False)
assert (libreria.validar_primer_nombre("juan carlos")==False)
assert (libreria.validar_primer_nombre("juan")==True)

assert (libreria.validar_codigo_trabajo("T1")==True)
assert (libreria.validar_codigo_trabajo("T2")==True)
assert (libreria.validar_nota(-4)==False)
assert (libreria.validar_nota(4)==True)

assert (libreria.validar_link("githut.com/juan/t1.git")==True)

assert (libreria.validar_entero("14")==False)

print("VAMONOS PERRAS! WOO!")


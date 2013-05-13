
import sys
from character import Character
from species import Species
from similarity import Similarity

from pylab import plot,show
from numpy import vstack,array
from numpy.random import rand
from scipy.cluster.vq import kmeans,vq


mancha = Character(1, 'Mancha', {'ausente':0, 'nao preenchida':1, 'preenchida':2})
pinta = Character(2, 'Pintas', {'ausente':0, 'presente':1})
m_super= Character(3, 'Membro Superior', {'ausente':0, 'presente':1})
m_infer = Character(4, 'Membro Inferior', {'ausente':0, 'presente':1})
qtd_membros = Character(5, 'Qtd de Membros', {'nenhum':0, 'um':1, 'dois':2, 'tres':3, 'quatro':4})
dedos = Character(6, 'Dedos', {'ausente':0, 'presente':1})
corpo= Character(7, 'Formato do Corpo', {'alongado':0, 'ovalado':1, 'redondo':2})
antena = Character(8, 'Antena',  {'ausente':0, 'presente':1})
olhos = Character(9, 'Olhos', {'ausente':0, 'presente':1})
cabeca = Character(10, 'Formato da Cabeca', {'achatada':0, 'redonda':1, 'triangular':2})
divisao = Character(11, 'Divisao do Corpo', {'continuo':0, 'segmentado':1})

# CRIACAO DAS ESPECIES
s2 = Species(2)
s2.choose_state(mancha, 'preenchida')
s2.choose_state(pinta, 'presente')
s2.choose_state(m_super, 'presente')
s2.choose_state(m_infer, 'presente')
s2.choose_state(qtd_membros, 'quatro')
s2.choose_state(dedos, 'presente')
s2.choose_state(corpo, 'ovalado')
s2.choose_state(antena, 'ausente')
s2.choose_state(olhos, 'presente')
s2.choose_state(cabeca, 'redonda')
s2.choose_state(divisao, 'segmentado')

s7 = Species(7)
s7.choose_state(mancha, 'ausente')
s7.choose_state(pinta, 'presente')
s7.choose_state(m_super, 'ausente')
s7.choose_state(m_infer, 'presente')
s7.choose_state(qtd_membros, 'um')
s7.choose_state(dedos, 'ausente')
s7.choose_state(corpo, 'ovalado')
s7.choose_state(antena, 'presente')
s7.choose_state(olhos, 'ausente')
s7.choose_state(cabeca, 'achatada')
s7.choose_state(divisao, 'segmentado')

s8 = Species(8)
s8.choose_state(mancha, 'ausente')
s8.choose_state(pinta, 'presente')
s8.choose_state(m_super, 'presente')
s8.choose_state(m_infer, 'presente')
s8.choose_state(qtd_membros, 'tres')
s8.choose_state(dedos, 'ausente')
s8.choose_state(corpo, 'ovalado')
s8.choose_state(antena, 'ausente')
s8.choose_state(olhos, 'ausente')
s8.choose_state(cabeca, 'achatada')
s8.choose_state(divisao, 'segmentado')

s16 = Species(16)
s16.choose_state(mancha, 'ausente')
s16.choose_state(pinta, 'presente')
s16.choose_state(m_super, 'presente')
s16.choose_state(m_infer, 'presente')
s16.choose_state(qtd_membros, 'quatro')
s16.choose_state(dedos, 'ausente')
s16.choose_state(corpo, 'redondo')
s16.choose_state(antena, 'ausente')
s16.choose_state(olhos, 'presente')
s16.choose_state(cabeca, 'achatada')
s16.choose_state(divisao, 'segmentado')

s18 = Species(18)
s18.choose_state(mancha, 'preenchida')
s18.choose_state(pinta, 'presente')
s18.choose_state(m_super, 'presente')
s18.choose_state(m_infer, 'presente')
s18.choose_state(qtd_membros, 'tres')
s18.choose_state(dedos, 'presente')
s18.choose_state(corpo, 'ovalado')
s18.choose_state(antena, 'ausente')
s18.choose_state(olhos, 'presente')
s18.choose_state(cabeca, 'redonda')
s18.choose_state(divisao, 'segmentado')

s19 = Species(19)
s19.choose_state(mancha, 'nao preenchida')
s19.choose_state(pinta, 'ausente')
s19.choose_state(m_super, 'presente')
s19.choose_state(m_infer, 'ausente')
s19.choose_state(qtd_membros, 'dois')
s19.choose_state(dedos, 'ausente')
s19.choose_state(corpo, 'alongado')
s19.choose_state(antena, 'presente')
s19.choose_state(olhos, 'presente')
s19.choose_state(cabeca, 'triangular')
s19.choose_state(divisao, 'segmentado')

s20 = Species(20)
s20.choose_state(mancha, 'nao preenchida')
s20.choose_state(pinta, 'ausente')
s20.choose_state(m_super, 'presente')
s20.choose_state(m_infer, 'ausente')
s20.choose_state(qtd_membros, 'dois')
s20.choose_state(dedos, 'ausente')
s20.choose_state(corpo, 'alongado')
s20.choose_state(antena, 'presente')
s20.choose_state(olhos, 'presente')
s20.choose_state(cabeca, 'triangular')
s20.choose_state(divisao, 'continuo')

#print s2.character_state(7).label
#print s20.states_array()

#print  Similarity.tanimoto(s19, s20)

c1 = [s2,s7, s8, s16, s18, s19, s20 ]
c2 = [s2,s7, s8, s16, s18, s19, s20 ]

data = vstack([c.states_array() for c in c1])
# data = vstack((rand(5,2) + array([.5,.5]),rand(5,2)))
#print data


# computing K-Means with K = 2 (2 clusters)
centroids,_ = kmeans(data,3)
print 'centroids'
print centroids

# assign each sample to a cluster
idx,cc = vq(data,centroids)
print 'indice de cada especie'
print cc


# some plotting using numpy's logical indexing
plot(data[idx==0,0],data[idx==0,1],'ob',
     data[idx==1,0],data[idx==1,1],'or')
plot(centroids[:,0],centroids[:,1],'sg',markersize=8)
#show()


for c in c1:
	for c_ in c2:
		coef = Similarity.intersection(c, c_)
#		print  '%d -> %d : %f' % (c.code, c_.code, coef)

## Caracteristiscas de uma especie
#for cs in s2.characters():
#	print cs[0].name + " -> " + cs[1].label

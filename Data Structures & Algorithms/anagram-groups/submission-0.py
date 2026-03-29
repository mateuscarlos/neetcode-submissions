class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Lista que guardará as nossas sublistas de anagramas
        groups = []
        
        # Função auxiliar para verificar se duas palavras são anagramas
        def is_anagram(s1, s2):
            if len(s1) != len(s2):
                return False
            return sorted(s1) == sorted(s2)

        for s in strs:
            found = False
            # Tentamos encaixar a palavra 's' num grupo existente
            for group in groups:
                # Comparamos 's' com a primeira palavra do grupo (representante)
                if is_anagram(s, group[0]):
                    group.append(s)
                    found = True
                    break
            
            # Se não encontramos nenhum grupo compatível, criamos um novo
            if not found:
                groups.append([s])
                
        return groups
        
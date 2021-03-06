from kqml import KQMLList
from tfta.tfta import TFTA
from tfta.tfta_module import TFTA_Module
from bioagents.tests.util import ekb_from_text, ekb_kstring_from_text, \
                                 get_request
from bioagents.tests.integration import _IntegrationTest, _FailureTest


#FIND-TF-TARGET
class _TestFindTfTarget(_IntegrationTest):
    def __init__(self, *args):
        super(_TestFindTfTarget, self).__init__(TFTA_Module)

    def create_message(self):
        # Here we create a KQML request that the TFTA needs to respond to
        tf = ekb_kstring_from_text(self.tf)
        content = KQMLList('FIND-TF-TARGET')
        content.set('tf', tf)
        return get_request(content), content

    def check_response_to_message(self, output):
        # Here we check the details of the response and make sure everything
        # we are looking for is in the output
        # First, we check that the response is a success
        assert output.head() == 'SUCCESS', output
        # Then we check that we got the expected number of target
        assert len(output.get('targets')) == 115
        # We could do further checks here to see if a given expected target
        # shows up in the response, etc.


#what genes are regulated by smad2?
class TestFindTfTarget1(_TestFindTfTarget):
    tf = 'SMAD2'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('targets')) == 115, output

#What genes does stat3 regulate?


#what genes are regulated by elk1 and smad2?
class TestFindTfTarget2(_TestFindTfTarget):
    tf = 'ELK1, SMAD2'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('targets')) == 28

#test IS-TF-TARGET
class _TestIsTfTarget(_IntegrationTest):
    def __init__(self, *args):
        super(_TestIsTfTarget, self).__init__(TFTA_Module)
    
    def create_message(self):
        # Here we create a KQML request that the TFTA needs to respond to
        tf = ekb_kstring_from_text(self.tf)
        target = ekb_kstring_from_text(self.target)
        content = KQMLList('IS-TF-TARGET')
        content.set('tf', tf)
        content.set('target', target)
        return get_request(content), content

#Does STAT3 regulate the c-fos gene?
class TestIsTfTarget1(_TestIsTfTarget):
    tf = 'STAT3'
    target = 'c-fos'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert output.gets('result') == 'TRUE', output
        
#TEST FIND-TARGET-TF
class _TestFindTargetTf(_IntegrationTest):
    def __init__(self, *args):
        super(_TestFindTargetTf, self).__init__(TFTA_Module)

    def create_message(self):
        # Here we create a KQML request that the TFTA needs to respond to
        target = ekb_kstring_from_text(self.target)
        content = KQMLList('FIND-TARGET-TF')
        content.set('target', target)
        return get_request(content), content

    def check_response_to_message(self, output):
        # Here we check the details of the response and make sure everything
        # we are looking for is in the output
        # First, we check that the response is a success
        assert output.head() == 'SUCCESS', output
        # Then we check that we got the expected number of target
        assert len(output.get('tfs')) == 116
        # We could do further checks here to see if a given expected target
        # shows up in the response, etc.

#Which transcription factors regulate frizzled8?
class TestFindTargetTf1(_TestFindTargetTf):
    target = 'frizzled8'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('tfs')) == 2, output

#What regulates SMURF2?
#What are the regulators of SMURF2?
class TestFindTargetTf2(_TestFindTargetTf):
    target = 'SMURF2'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('tfs')) == 3
    
#TEST FIND-PATHWAY-GENE
class _TestFindPathwayGene(_IntegrationTest):
    def __init__(self, *args):
        super(_TestFindPathwayGene, self).__init__(TFTA_Module)

    def create_message(self):
        # Here we create a KQML request that the TFTA needs to respond to
        gene = ekb_kstring_from_text(self.gene)
        content = KQMLList('FIND-PATHWAY-GENE')
        content.set('gene', gene)
        return get_request(content), content
        
#What pathways involve SRF?
class TestFindPathwayGene1(_TestFindPathwayGene):
    gene = 'SRF'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('pathways')) == 27, output
        
#What pathways involve kras and elk1?
class TestFindPathwayGene2(_TestFindPathwayGene):
    gene = 'KRAS, ELK1'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('pathways')) == 23, output

#TEST FIND-PATHWAY-DB-GENE
class _TestFindPathwayDBGene(_IntegrationTest):
    def __init__(self, *args):
        super(_TestFindPathwayDBGene, self).__init__(TFTA_Module)

    def create_message(self):
        # Here we create a KQML request that the TFTA needs to respond to
        gene = ekb_kstring_from_text(self.gene)
        db = self.database
        content = KQMLList('FIND-PATHWAY-DB-GENE')
        content.set('gene', gene)
        content.set('database', db)
        return get_request(content), content
        
#Which Reactome pathways utilize SRF?
class TestFindPathwayDBGene1(_TestFindPathwayDBGene):
    gene = 'SRF'
    database = 'Reactome'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('pathways')) == 4, output
        
#Which KEGG pathways utilize SRF?
class TestFindPathwayDBGene2(_TestFindPathwayDBGene):
    gene = 'SRF'
    database = 'KEGG'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('pathways')) == 4, output

#TEST FIND-TF-PATHWAY
class _TestFindTfPathway(_IntegrationTest):
    def __init__(self, *args):
        super(_TestFindTfPathway, self).__init__(TFTA_Module)

    def create_message(self):
        # Here we create a KQML request that the TFTA needs to respond to
        pathway = ekb_kstring_from_text(self.pathway)
        content = KQMLList('FIND-TF-PATHWAY')
        content.set('pathway', pathway)
        return get_request(content), content
        
#Which transcription factors are in the MAPK signaling pathway?
class TestFindTfPathway1(_TestFindTfPathway):
    pathway = 'MAPK'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('pathways')) == 17, output
        
#TEST FIND-GENE-PATHWAY
class _TestFindGenePathway(_IntegrationTest):
    def __init__(self, *args):
        super(_TestFindGenePathway, self).__init__(TFTA_Module)

    def create_message(self):
        # Here we create a KQML request that the TFTA needs to respond to
        pathway = ekb_kstring_from_text(self.pathway)
        content = KQMLList('FIND-GENE-PATHWAY')
        content.set('pathway', pathway)
        return get_request(content), content
        
#What genes are in the MAPK signaling pathway?
class TestFindGenePathway1(_TestFindGenePathway):
    pathway = 'MAPK'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('pathways')) == 23, output
        
#What genes are involved in the il-12 pathway?
class TestFindGenePathway2(_TestFindGenePathway):
    pathway = 'il-12'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('pathways')) == 3, output
        
#What genes are in the immune system pathway?
class TestFindGenePathway3(_TestFindGenePathway):
    pathway = 'immune system'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('pathways')) == 4, output
        
#TEST FIND-PATHWAY-KEYWORD
class _TestFindPathwayKeyword(_IntegrationTest):
    def __init__(self, *args):
        super(_TestFindPathwayKeyword, self).__init__(TFTA_Module)

    def create_message(self):
        # Here we create a KQML request that the TFTA needs to respond to
        keyword = self.keyword
        content = KQMLList('FIND-PATHWAY-KEYWORD')
        content.set('keyword', keyword)
        return get_request(content), content

#What pathways involve calcium?
class TestFindPathwayKeyword1(_TestFindPathwayKeyword):
    keyword = 'calcium'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('pathways')) == 10, output
        
#FIND-TF-KEYWORD
class _TestFindTfKeyword(_IntegrationTest):
    def __init__(self, *args):
        super(_TestFindTfKeyword, self).__init__(TFTA_Module)

    def create_message(self):
        # Here we create a KQML request that the TFTA needs to respond to
        keyword = self.keyword
        content = KQMLList('FIND-TF-KEYWORD')
        content.set('keyword', keyword)
        return get_request(content), content

#What transcription factors are in the calcium regulated pathways?
class TestFindTfKeyword1(_TestFindTfKeyword):
    keyword = 'calcium'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        print('numPathways=' + str(len(output.get('pathways'))))
        assert len(output.get('pathways')) == 6, output
        
#TEST FIND-COMMON-TF-GENES
class _TestFindCommonTfGene(_IntegrationTest):
    def __init__(self, *args):
        super(_TestFindCommonTfGene, self).__init__(TFTA_Module)

    def create_message(self):
        # Here we create a KQML request that the TFTA needs to respond to
        target = ekb_kstring_from_text(self.target)
        content = KQMLList('FIND-COMMON-TF-GENES')
        content.set('target', target)
        return get_request(content), content
        
#What transcription factors are shared by the SRF, HRAS, and elk1 genes?
class TestFindCommmonTfGene1(_TestFindCommonTfGene):
    target = 'SRF, HRAS, elk1'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('tfs')) == 2, output
        
#What transcription factors are in common to the STAT3, SOCS3, and CREB5 genes?
class TestFindCommonTfGene2(_TestFindCommonTfGene):
    target = 'STAT3, SOCS3, CREB5'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        print('numTFs=' + str(len(output.get('tfs'))))
        assert len(output.get('tfs')) == 2, output
        
#TEST FIND-COMMON-PATHWAY-GENES
class _TestFindCommonPathwayGene(_IntegrationTest):
    def __init__(self, *args):
        super(_TestFindCommonPathwayGene, self).__init__(TFTA_Module)

    def create_message(self):
        # Here we create a KQML request that the TFTA needs to respond to
        target = ekb_kstring_from_text(self.target)
        content = KQMLList('FIND-COMMON-PATHWAY-GENES')
        content.set('target', target)
        return get_request(content), content
        
#Which pathways are shared by STAT3, SOCS3, IFNG, FOXO3, and CREB5 genes?
class TestFindCommonPathwayGene1(_TestFindCommonPathwayGene):
    target = 'STAT3, SOCS3, IFNG, FOXO3, CREB5'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        print('numPathways=' + str(len(output.get('pathways'))))
        assert len(output.get('pathways')) == 69, output
        
#What signaling pathways are shared by STAT3 and SRF?
class TestFindCommonPathwayGene2(_TestFindCommonPathwayGene):
    target = 'STAT3, SRF'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('pathways')) == 6, output

#TEST FIND-PATHWAY-GENE-KEYWORD
class _TestFindPathwayGeneKeyword(_IntegrationTest):
    def __init__(self, *args):
        super(_TestFindPathwayGeneKeyword, self).__init__(TFTA_Module)

    def create_message(self):
        # Here we create a KQML request that the TFTA needs to respond to
        gene = ekb_kstring_from_text(self.gene)
        keyword = self.keyword
        content = KQMLList('FIND-PATHWAY-GENE-KEYWORD')
        content.set('gene', gene)
        content.set('keyword', keyword)
        return get_request(content), content
        
#What immune pathways involve kras and elk1?
class TestFindPathwayGeneKeyword1(_TestFindPathwayGeneKeyword):
    gene = 'kras, elk1'
    keyword = 'immune'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('pathways')) == 2, output
        
#What immune pathways involve tap1 and jak1?
class TestFindPathwayGeneKeyword2(_TestFindPathwayGeneKeyword):
    gene = 'tap1, jak1'
    keyword = 'immune'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('pathways')) == 1, output

#TEST FIND-COMMON-PATHWAY-GENES-KEYWORD
class _TestFindCommonPathwayGeneKeyword(_IntegrationTest):
    def __init__(self, *args):
        super(_TestFindCommonPathwayGeneKeyword, self).__init__(TFTA_Module)

    def create_message(self):
        # Here we create a KQML request that the TFTA needs to respond to
        gene = ekb_kstring_from_text(self.gene)
        keyword = self.keyword
        content = KQMLList('FIND-COMMON-PATHWAY-GENES-KEYWORD')
        content.set('gene', gene)
        content.set('keyword', keyword)
        return get_request(content), content
        
#Which immune pathways are shared by STAT3, SOCS3, and CREB5 genes?
class TestFindCommonPathwayGeneKeyword1(_TestFindCommonPathwayGeneKeyword):
    gene = 'STAT3, SOCS3, CREB5'
    keyword = 'immune'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('pathways')) == 2, output
        
#TEST IS-PATHWAY-GENE
class _TestIsPathwayGene(_IntegrationTest):
    def __init__(self, *args):
        super(_TestIsPathwayGene, self).__init__(TFTA_Module)

    def create_message(self):
        # Here we create a KQML request that the TFTA needs to respond to
        gene = ekb_kstring_from_text(self.gene)
        pathway = ekb_kstring_from_text(self.pathway)
        content = KQMLList('IS-PATHWAY-GENE')
        content.set('gene', gene)
        content.set('pathway', pathway)
        return get_request(content), content
        
#Does the mTor pathway utilize SGK1?
class TestIsPathwayGene1(_TestIsPathwayGene):
    gene = 'SGK1'
    pathway = 'mTor pathway'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('pathways')) == 3, output
        
#TEST IS-TF-TARGET-TISSUE
class _TestIsTfTargetTissue(_IntegrationTest):
    def __init__(self, *args):
        super(_TestIsTfTargetTissue, self).__init__(TFTA_Module)
    
    def create_message(self):
        # Here we create a KQML request that the TFTA needs to respond to
        tf = ekb_kstring_from_text(self.tf)
        print('tf=' + str(tf))
        target = ekb_kstring_from_text(self.target)
        print('target=' + str(target))
        tissue = self.tissue
        content = KQMLList('IS-TF-TARGET-TISSUE')
        content.set('tf', tf)
        content.set('target', target)
        content.set('tissue', tissue)
        print('content=' + str(content))
        print('get_request(content)=' + str(get_request(content)))
        return get_request(content), content

#Does STAT3 regulate the JUN gene in the lung?
class TestIsTfTargetTissue1(_TestIsTfTargetTissue):
    #since trips parser cannot recognize JUN as a gene, so instead try
    #c-JUN or JUN gene
    tf = 'STAT3'
    target = 'c-JUN'
    tissue = 'lung'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert output.gets('result') == 'TRUE', output
        
#Does STAT3 regulate the c-fos gene in the liver?
class TestIsTfTargetTissue2(_TestIsTfTargetTissue):
    tf = 'STAT3'
    target = 'c-fos'
    tissue = 'liver'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert output.gets('result') == 'FALSE', output

#Does STAT3 regulate the cfos gene in the lung?
class TestIsTfTargetTissue3(_TestIsTfTargetTissue):
    tf = 'STAT3'
    target = 'c-fos'
    tissue = 'lung'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert output.gets('result') == 'TRUE', output

#TEST FIND-TF-TARGET-TISSUE
class _TestFindTfTargetTissue(_IntegrationTest):
    def __init__(self, *args):
        super(_TestFindTfTargetTissue, self).__init__(TFTA_Module)

    def create_message(self):
        # Here we create a KQML request that the TFTA needs to respond to
        tf = ekb_kstring_from_text(self.tf)
        tissue = self.tissue
        content = KQMLList('FIND-TF-TARGET-TISSUE')
        content.set('tf', tf)
        content.set('tissue', tissue)
        return get_request(content), content

    def check_response_to_message(self, output):
        # First, we check that the response is a success
        assert output.head() == 'SUCCESS', output
        # Then we check that we got the expected number of target
        assert len(output.get('targets')) == 115

#What genes does stat3 regulate in lung?
class TestFindTfTargetTissue1(_TestFindTfTargetTissue):
    tf = 'STAT3'
    tissue = 'lung'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('targets')) == 57, output

#What genes does stat3 regulate in liver?
class TestFindTfTargetTissue2(_TestFindTfTargetTissue):
    tf = 'STAT3'
    tissue = 'liver'
    def check_response_to_message(self, output):
        assert output.head() == 'FAILURE', output
        assert output.get('reason') == 'NO_TARGET_FOUND', output

#TEST FIND-TARGET-TF-TISSUE
class _TestFindTargetTfTissue(_IntegrationTest):
    def __init__(self, *args):
        super(_TestFindTargetTfTissue, self).__init__(TFTA_Module)

    def create_message(self):
        # Here we create a KQML request that the TFTA needs to respond to
        target = ekb_kstring_from_text(self.target)
        tissue = self.tissue
        content = KQMLList('FIND-TARGET-TF-TISSUE')
        content.set('target', target)
        content.set('tissue', tissue)
        return get_request(content), content

    def check_response_to_message(self, output):
        # First, we check that the response is a success
        assert output.head() == 'SUCCESS', output
        # Then we check that we got the expected number of target
        assert len(output.get('tfs')) == 116

#Which transcription factors regulate frizzled8 in liver?
class TestFindTargetTfTissue1(_TestFindTargetTfTissue):
    target = 'frizzled8'
    tissue = 'liver'
    def check_response_to_message(self, output):
        assert output.head() == 'FAILURE', output
        assert output.get('reason') == 'TARGET_NOT_FOUND', output

#Which transcription factors regulate mapk14 in bladder?
class TestFindTargetTfTissue2(_TestFindTargetTfTissue):
    target = 'mapk14'
    tissue = 'bladder'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('tfs')) == 5, output

#Which transcription factors regulate ELK1 in brain?
class TestFindTargetTfTissue3(_TestFindTargetTfTissue):
    target = 'ELK1'
    tissue = 'brain'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('tfs')) == 55, output
        
#TEST IS-MIRNA-TARGET
class _TestIsMirnaTarget(_IntegrationTest):
    def __init__(self, *args):
        super(_TestIsMirnaTarget, self).__init__(TFTA_Module)

    def create_message(self):
        # Here we create a KQML request that the TFTA needs to respond to
        target = ekb_kstring_from_text(self.target)
        mirna = ekb_kstring_from_text(self.mirna)
        content = KQMLList('IS-MIRNA-TARGET')
        content.set('target', target)
        content.set('miRNA', mirna)
        return get_request(content), content
        
#Does miR-20b-5p target STAT3?
class TestIsMirnaTarget1(_TestIsMirnaTarget):
    target = 'STAT3'
    mirna = 'miR-20b-5p'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert output.get('is-miRNA-target') == 'TRUE', output
        
#TEST FIND-TARGET-MIRNA
class _TestFindTargetMirna(_IntegrationTest):
    def __init__(self, *args):
        super(_TestFindTargetMirna, self).__init__(TFTA_Module)

    def create_message(self):
        # Here we create a KQML request that the TFTA needs to respond to
        mirna = ekb_kstring_from_text(self.mirna)
        content = KQMLList('FIND-TARGET-MIRNA')
        content.set('miRNA', mirna)
        return get_request(content), content
        
#What genes does miR-20b-5p target?
class TestFindTargetMirna1(_TestFindTargetMirna):
    mirna = 'miR-20b-5p'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('targets')) == 917, output

#What genes are regulated by miR-20b-5p and MIR-29B-1-5P? (Don't work)
class TestFindTargetMirna2(_TestFindTargetMirna):
    mirna = 'miR-20b-5p, MIR-29B-1-5P'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('targets')) == 12, output
        
#TEST FIND-MIRNA-TARGET
class _TestFindMirnaTarget(_IntegrationTest):
    def __init__(self, *args):
        super(_TestFindMirnaTarget, self).__init__(TFTA_Module)

    def create_message(self):
        # Here we create a KQML request that the TFTA needs to respond to
        target = ekb_kstring_from_text(self.target)
        content = KQMLList('FIND-MIRNA-TARGET')
        content.set('target', target)
        return get_request(content), content
        
#What microRNAs target STAT3?
class TestFindMirnaTarget1(_TestFindMirnaTarget):
    target = 'STAT3'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('miRNAs')) == 80, output

#TEST FIND-MIRNA-COUNT-GENE
class _TestFindMirnaCountGene(_IntegrationTest):
    def __init__(self, *args):
        super(_TestFindMirnaCountGene, self).__init__(TFTA_Module)

    def create_message(self):
        # Here we create a KQML request that the TFTA needs to respond to
        target = ekb_kstring_from_text(self.target)
        content = KQMLList('FIND-MIRNA-COUNT-GENE')
        content.set('target', target)
        return get_request(content), content
        
#What miRNAs most frequently regulate EGFR, SRF, STAT3, JAK2, and SMAD3?
class TestFindMirnaCountGene1(_TestFindMirnaCountGene):
    target = 'EGFR, SRF, STAT3, JAK2, SMAD3'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('miRNAs')) == 23, output
        
#FIND-GENE-COUNT-MIRNA
class _TestFindGeneCountMirna(_IntegrationTest):
    def __init__(self, *args):
        super(_TestFindGeneCountMirna, self).__init__(TFTA_Module)

    def create_message(self):
        # Here we create a KQML request that the TFTA needs to respond to
        mirna = ekb_kstring_from_text(self.mirna)
        content = KQMLList('FIND-GENE-COUNT-MIRNA')
        content.set('miRNA', mirna)
        return get_request(content), content
        
#What genes are most frequently regulated by miR-335-5p, miR-155-5p, miR-145-5p, and miR-20a-5p?
class TestFindGeneCountMirna1(_TestFindGeneCountMirna):
    mirna = 'miR-335-5p, miR-155-5p, miR-145-5p, miR-20a-5p'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('targets')) == 380, output

#What genes are most frequently regulated by miR-335-5p, miR-155-5p and miR-145-5p?
class TestFindGeneCountMirna2(_TestFindGeneCountMirna):
    mirna = 'miR-335-5p, miR-155-5p, miR-145-5p'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('targets')) == 151, output

#TEST FIND-PATHWAY-DB-KEYWORD
class _TestFindPathwayDbKeyword(_IntegrationTest):
    def __init__(self, *args):
        super(_TestFindPathwayDbKeyword, self).__init__(TFTA_Module)

    def create_message(self):
        # Here we create a KQML request that the TFTA needs to respond to
        database = self.database
        keyword = self.keyword
        content = KQMLList('FIND-PATHWAY-DB-KEYWORD')
        content.set('database', database)
        content.set('keyword', keyword)
        return get_request(content), content
        
#What KEGG pathways involve immune signaling?
class TestFindPathwayDbKeyword1(_TestFindPathwayDbKeyword):
    database = 'KEGG'
    keyword = 'immune'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('pathways')) == 2, output
        
#What KEGG pathways involve immune system?
class TestFindPathwayDbKeyword2(_TestFindPathwayDbKeyword):
    database = 'KEGG'
    keyword = 'immune system'
    def check_response_to_message(self, output):
        assert output.head() == 'FAILURE', output
        assert output.get('reason') == 'PathwayNotFoundException', output
        
# What reactome pathways involve immune system?
class TestFindPathwayDbKeyword3(_TestFindPathwayDbKeyword):
    database = 'reactome'
    keyword = 'immune system'
    def check_response_to_message(self, output):
        assert output.head() == 'SUCCESS', output
        assert len(output.get('pathways')) == 4, output
        
##test wrong message sent to TFTA
#What genes are regulated by elk1 and srf?
#This query should send query to find-target for new ba or find-tf-target, but now we take 
#it as a find-target-mirna query
class TestFindTargetMirna3(_TestFindTargetMirna):
    mirna = 'ELK1, SRF'
    def check_response_to_message(self, output):
        assert output.head() == 'FAILURE', output
        assert output.get('reason') == 'MIRNA_NOT_FOUND', output


if __name__ == '__main__':
    TestFindTfTarget1().run_test()
    
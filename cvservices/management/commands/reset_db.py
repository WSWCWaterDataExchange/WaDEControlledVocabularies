from django.core.management.base import BaseCommand, CommandError
from cvservices.models import AggregationStatistic, CropType, EPSGCode, GNISFeatureName, IrrigationMethod, \
 LegalStatus, MethodType, NAICSCode, \
 NHDNetworkStatus, NHDProduct	,RegulatoryStatus, ReportingUnitType, ReportYear	, ReportYearType	,SiteType,Units	,\
USGSCategory	,Variable	,VariableSpecific	,WaterAllocationBasis	,WaterQualityIndicator	,WaterRightType	,WaterSourceType	

class Command(BaseCommand):
    help = 'Deletes every object in the database'

    #def add_arguments(self, parser):
    #    pass

    def handle(self, *args, **options):

        for object in AggregationStatistic.objects.all():
            object.delete()

        for object in CropType.objects.all():
            object.delete()
  
        for object in EPSGCode.objects.all():
            object.delete()

        for object in GNISFeatureName.objects.all():
            object.delete()

        for object in IrrigationMethod.objects.all():
            object.delete()

        for object in LegalStatus.objects.all():
            object.delete()

        for object in MethodType.objects.all():
            object.delete()

        for object in NAICSCode.objects.all():
            object.delete()

        for object in NHDNetworkStatus.objects.all():
            object.delete()

        for object in NHDProduct.objects.all():
            object.delete()

        for object in RegulatoryStatus.objects.all():
            object.delete()

        for object in ReportingUnitType.objects.all():
            object.delete()

        for object in ReportYear.objects.all():
            object.delete()

        for object in ReportYearType.objects.all():
            object.delete()
   
        for object in Units.objects.all():
            object.delete()
   
        for object in USGSCategory.objects.all():
            object.delete()  
   
        for object in Variable.objects.all():
            object.delete()
         
        for object in VariableSpecific.objects.all():
            object.delete()
          
        for object in WaterAllocationBasis.objects.all():
            object.delete()          
          
        for object in WaterQualityIndicator.objects.all():
            object.delete()         

        for object in WaterRightType.objects.all():
            object.delete()     
          
        for object in WaterSourceType.objects.all():
            object.delete() 
          

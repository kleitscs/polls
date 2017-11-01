import datetime
from django.utils import timezone

from django.db import models
from django.forms import ModelForm

from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


@python_2_unicode_compatible
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
# @python_2_unicode_compatible
# class Characteristicvalues(models.Model):
#     characteristicvalue = models.AutoField(db_column='CharacteristicValueID', primary_key=True)
#     measurementunit = models.ForeignKey('Measurementunit', models.DO_NOTHING, db_column='MeasurementUnitID')
#     minvalue = models.DecimalField(db_column='MinValue', max_digits=10, decimal_places=4, blank=True, null=True)
#     maxvalue = models.DecimalField(db_column='MaxValue', max_digits=10, decimal_places=4, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'CharacteristicValues'
#
# @python_2_unicode_compatible
# class Characteristics(models.Model):
#     characteristic = models.AutoField(db_column='CharacteristicID', primary_key=True)
#     characteristicname = models.CharField(db_column='CharacteristicName', unique=True, max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'Characteristics'
#
# @python_2_unicode_compatible
# class Company(models.Model):
#     company = models.AutoField(db_column='CompanyID', primary_key=True)
#     name = models.CharField(db_column='Name', max_length=50)
#     isvendor = models.IntegerField(db_column='IsVendor')
#     iscarrier = models.IntegerField(db_column='IsCarrier')
#     iscustomer = models.IntegerField(db_column='IsCustomer')
#
#     class Meta:
#         managed = False
#         db_table = 'Company'
#
# @python_2_unicode_compatible
# class Costmultiplierforcustomer(models.Model):
#     costmultiplierforcustomer = models.AutoField(db_column='CostMultiplierForCustomerID', primary_key=True)
#     customertype = models.ForeignKey('Customertype', models.DO_NOTHING, db_column='CustomerTypeID')
#     multipliervalue = models.DecimalField(db_column='MultiplierValue', max_digits=4, decimal_places=2)
#
#     class Meta:
#         managed = False
#         db_table = 'CostMultiplierForCustomer'
#
# @python_2_unicode_compatible
# class Costmultiplierforoperationtype(models.Model):
#     costmultiplierforoperationtype = models.AutoField(db_column='CostMultiplierForOperationTypeID', primary_key=True)
#     processoperationtype = models.ForeignKey('Processoperationtype', models.DO_NOTHING, db_column='ProcessOperationTypeID')
#     threaddiameterinchequivalentmin = models.DecimalField(db_column='ThreadDiameterInchEquivalentMin', max_digits=6, decimal_places=4)
#     threaddiameterinchequivalentmax = models.DecimalField(db_column='ThreadDiameterInchEquivalentMax', max_digits=6, decimal_places=4)
#     multipliervalue = models.DecimalField(db_column='MultiplierValue', max_digits=4, decimal_places=2)
#
#     class Meta:
#         managed = False
#         db_table = 'CostMultiplierForOperationType'
#
# @python_2_unicode_compatible
# class Costmultiplierforthread(models.Model):
#     costmultiplierforthread = models.AutoField(db_column='CostMultiplierForThreadID', primary_key=True)
#     threaddiameter = models.ForeignKey('Threaddiameter', models.DO_NOTHING, db_column='ThreadDiameterID')
#     pitchthreaddiameterdesignation = models.ForeignKey('Pitchthreaddiameterdesignation', models.DO_NOTHING, db_column='PitchThreadDiameterDesignationID')
#     multipliervalue = models.DecimalField(db_column='MultiplierValue', max_digits=4, decimal_places=2)
#
#     class Meta:
#         managed = False
#         db_table = 'CostMultiplierForThread'
#
# @python_2_unicode_compatible
# class Customertype(models.Model):
#     customertype = models.AutoField(db_column='CustomerTypeID', primary_key=True)
#     name = models.CharField(db_column='Name', max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'CustomerType'
#
# @python_2_unicode_compatible
# class Datachemistry(models.Model):
#     datachemistry = models.AutoField(db_column='DataChemistryID', primary_key=True)
#     carbonmax = models.DecimalField(db_column='CarbonMax', max_digits=10, decimal_places=4, blank=True, null=True)
#     maganesemin = models.DecimalField(db_column='MaganeseMin', max_digits=10, decimal_places=4, blank=True, null=True)
#     sulfurmax = models.DecimalField(db_column='SulfurMax', max_digits=10, decimal_places=4, blank=True, null=True)
#     phosphorusmax = models.DecimalField(db_column='PhosphorusMax', max_digits=10, decimal_places=4, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'DataChemistry'
#
# @python_2_unicode_compatible
# class Datadimentional(models.Model):
#     datadimentional = models.AutoField(db_column='DataDimentionalID', primary_key=True)
#     widthacrossflatsmax = models.DecimalField(db_column='WidthAcrossFlatsMax', max_digits=10, decimal_places=4)
#     widthacrossflatsmin = models.DecimalField(db_column='WidthAcrossFlatsMin', max_digits=10, decimal_places=4)
#     widthacrosscornersmax = models.DecimalField(db_column='WidthAcrossCornersMax', max_digits=10, decimal_places=4)
#     widthacrosscornersmin = models.DecimalField(db_column='WidthAcrossCornersMin', max_digits=10, decimal_places=4, blank=True, null=True)
#     thicknessmax = models.DecimalField(db_column='ThicknessMax', max_digits=10, decimal_places=4)
#     thicknessmin = models.DecimalField(db_column='ThicknessMin', max_digits=10, decimal_places=4, blank=True, null=True)
#     wrenchingheightmin = models.DecimalField(db_column='WrenchingHeightMin', max_digits=10, decimal_places=4, blank=True, null=True)
#     countersinkmax = models.DecimalField(db_column='CounterSinkMax', max_digits=10, decimal_places=4, blank=True, null=True)
#     bearingdiametermin = models.DecimalField(db_column='BearingDiameterMin', max_digits=10, decimal_places=4, blank=True, null=True)
#     axialrunoutmax = models.DecimalField(db_column='AxialRunoutMax', max_digits=10, decimal_places=4, blank=True, null=True)
#     flangediamatermax = models.DecimalField(db_column='FlangeDiamaterMax', max_digits=10, decimal_places=4, blank=True, null=True)
#     flangediamatermin = models.DecimalField(db_column='FlangeDiamaterMin', max_digits=10, decimal_places=4, blank=True, null=True)
#     flangethiknessmin = models.DecimalField(db_column='FlangeThiknessMin', max_digits=10, decimal_places=4, blank=True, null=True)
#     flangetopradiusmax = models.DecimalField(db_column='FlangeTopRadiusMax', max_digits=10, decimal_places=4, blank=True, null=True)
#     bcmin = models.DecimalField(db_column='BCMin', max_digits=10, decimal_places=4, blank=True, null=True)
#     threadhightmin = models.DecimalField(db_column='ThreadHightMin', max_digits=10, decimal_places=4, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'DataDimentional'
#
# @python_2_unicode_compatible
# class Datamechanicalperformance(models.Model):
#     datamechanicperformance = models.AutoField(db_column='DataMechanicPerformanceID', primary_key=True)
#     proofloadmin = models.IntegerField(db_column='ProofLoadMin')
#     hardnessmin = models.IntegerField(db_column='HardnessMin', blank=True, null=True)
#     hardnessmax = models.IntegerField(db_column='HardnessMax')
#     hardnessunit = models.ForeignKey('Hardnessunit', models.DO_NOTHING, db_column='HardnessUnitID')
#
#     class Meta:
#         managed = False
#         db_table = 'DataMechanicalPerformance'
#
# @python_2_unicode_compatible
# class Datapackaging(models.Model):
#     characteristic = models.ForeignKey(Characteristics, models.DO_NOTHING, db_column='CharacteristicID', blank=True, null=True)
#     datapackaging = models.AutoField(db_column='DataPackagingID', primary_key=True)
#
#     class Meta:
#         managed = False
#         db_table = 'DataPackaging'
#
# @python_2_unicode_compatible
# class Datathreadinspection(models.Model):
#     datathreadinspection = models.AutoField(db_column='DataThreadInspectionID', primary_key=True)
#     threadtoleranceclass = models.ForeignKey('Threadtoleranceclass', models.DO_NOTHING, db_column='ThreadToleranceClassID')
#     gogageinspectionmin = models.DecimalField(db_column='GoGageInspectionMin', max_digits=5, decimal_places=2, blank=True, null=True)
#     nogogageinspectionmax = models.DecimalField(db_column='NoGoGageInspectionMax', max_digits=5, decimal_places=2, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'DataThreadInspection'
#
# @python_2_unicode_compatible
# class Datathreadtolerance(models.Model):
#     datathreadtolerance = models.AutoField(db_column='DataThreadToleranceID', primary_key=True)
#     threadtoleranceclass = models.ForeignKey('Threadtoleranceclass', models.DO_NOTHING, db_column='ThreadToleranceClassID')
#     minordiametermin = models.DecimalField(db_column='MinorDiameterMin', max_digits=12, decimal_places=6)
#     minordiametermax = models.DecimalField(db_column='MinorDiameterMax', max_digits=12, decimal_places=6)
#     pitchdiametermin = models.DecimalField(db_column='PitchDiameterMin', max_digits=12, decimal_places=6)
#     pitchdiametermax = models.DecimalField(db_column='PitchDiameterMax', max_digits=12, decimal_places=6)
#
#     class Meta:
#         managed = False
#         db_table = 'DataThreadTolerance'
#
# @python_2_unicode_compatible
# class Datatorqperformance(models.Model):
#     datatorqperformance = models.AutoField(db_column='DataTorqPerformanceID', primary_key=True)
#     class_field = models.CharField(db_column='Class', max_length=50, blank=True, null=True) Field renamed because it was a Python reserved word.
#     breakloosetorqmin = models.DecimalField(db_column='BreakLooseTorqMin', max_digits=10, decimal_places=4, blank=True, null=True)
#     firstinstallationtorqmax = models.DecimalField(db_column='FirstInstallationTorqMax', max_digits=10, decimal_places=4, blank=True, null=True)
#     firstremovaltorqmin = models.DecimalField(db_column='FirstRemovalTorqMin', max_digits=10, decimal_places=4, blank=True, null=True)
#     thirdremovaltorqmin = models.DecimalField(db_column='ThirdRemovalTorqMin', max_digits=10, decimal_places=4, blank=True, null=True)
#     fithremovaltorqmin = models.DecimalField(db_column='FithRemovalTorqMin', max_digits=10, decimal_places=4, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'DataTorqPerformance'
#
# @python_2_unicode_compatible
# class Designation(models.Model):
#     designation = models.IntegerField(db_column='DesignationID', primary_key=True)
#     name = models.CharField(db_column='Name', max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'Designation'
#
# @python_2_unicode_compatible
# class Frieghtinfoprice(models.Model):
#     frieghtinfoprice = models.AutoField(db_column='FrieghtInfoPriceID', primary_key=True)
#     frieghtinfo = models.ForeignKey('Frieghtinfo', models.DO_NOTHING, db_column='FrieghtInfoID')
#     weightmax = models.IntegerField(db_column='WeightMax')
#     priceper100lb = models.DecimalField(db_column='PricePer100Lb', max_digits=10, decimal_places=4)
#
#     class Meta:
#         managed = False
#         db_table = 'FrieghtInfoPrice'
#
# @python_2_unicode_compatible
# class Hardnessunit(models.Model):
#     hardnessunit = models.AutoField(db_column='HardnessUnitID', primary_key=True)
#     name = models.CharField(db_column='Name', max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'HardnessUnit'


@python_2_unicode_compatible
class Measurementunit(models.Model):
    measurementunit = models.AutoField(db_column='MeasurementUnitID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=50)

    class Meta:
        managed = False
        db_table = 'MeasurementUnit'

    def __str__(self):
        return self.name
# @python_2_unicode_compatible
# class Organization(models.Model):
#     organization = models.AutoField(db_column='OrganizationID', primary_key=True)
#     name = models.CharField(db_column='Name', max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'Organization'
#
# @python_2_unicode_compatible
# class Packingcartontype(models.Model):
#     packingcartontype = models.IntegerField(db_column='PackingCartonTypeID', primary_key=True)
#     name = models.CharField(db_column='Name', max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'PackingCartonType'
#
# @python_2_unicode_compatible
# class Packinglabeltype(models.Model):
#     packinglabeltype = models.IntegerField(db_column='PackingLabelTypeID', primary_key=True)
#     name = models.CharField(db_column='Name', max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'PackingLabelType'
#
# @python_2_unicode_compatible
# class Packingwaxtype(models.Model):
#     packingwaxtype = models.IntegerField(db_column='PackingWaxTypeID', primary_key=True)
#     name = models.CharField(db_column='Name', max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'PackingWaxType'
#
# @python_2_unicode_compatible
# class Parentchild(models.Model):
#     purchasepart = models.CharField(db_column='PurchasePart', max_length=36, blank=True, null=True)
#     purchasepartcode = models.CharField(db_column='PurchasePartCode', max_length=2, blank=True, null=True)
#     salespart = models.CharField(db_column='SalesPart', max_length=36, blank=True, null=True)
#     salespartcode = models.CharField(db_column='SalesPartCode', max_length=2, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ParentChild'


@python_2_unicode_compatible
class Partnumber(models.Model):
    partnumber = models.AutoField(db_column='PartNumberID', primary_key=True)
    threaddesignation = models.ForeignKey('Threaddesignation', models.DO_NOTHING, db_column='ThreadDesignationID', blank=True, null=True)
    # steel = models.ForeignKey('Steel', models.DO_NOTHING, db_column='SteelID', blank=True, null=True)
    # torquetf = models.ForeignKey('Torquetf', models.DO_NOTHING, db_column='TorqueTFID', blank=True, null=True)
    # standardspecplating = models.ForeignKey('Standardspecplating', models.DO_NOTHING, db_column='StandardSpecPlatingID', blank=True, null=True)
    name = models.CharField(db_column='Name', unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'PartNumber'

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class Pitch(models.Model):
    pitch = models.AutoField(db_column='PitchID', primary_key=True)
    name = models.CharField(db_column='Name', unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'Pitch'

    def __str__(self):
        return self.name

@python_2_unicode_compatible
class Pitch2Threaddiameter(models.Model):
    pitch = models.ForeignKey(Pitch, models.DO_NOTHING, db_column='PitchID')
    threaddiameter = models.ForeignKey('Threaddiameter', models.DO_NOTHING, db_column='ThreadDiameterID')
    pitch2threaddiameter = models.AutoField(db_column='Pitch2ThreadDiameterID', primary_key=True)

    class Meta:
        managed = False
        db_table = 'Pitch2ThreadDiameter'
        # unique_together = (('pitchid', 'threaddiameterid'),)

    def __str__(self):
        return


@python_2_unicode_compatible
class Pitchthreaddiameterdesignation(models.Model):
    pitchthreaddiameterdesignation = models.AutoField(db_column='PitchThreadDiameterDesignationID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=20)

    class Meta:
        managed = False
        db_table = 'PitchThreadDiameterDesignation'

    def __str__(self):
        return self.name

# @python_2_unicode_compatible
# class Platingsupplier(models.Model):
#     platingsupplier = models.AutoField(db_column='PlatingSupplierID', primary_key=True)
#     vendorcompany = models.ForeignKey(Company, models.DO_NOTHING, db_column='VendorCompanyID')
#     characteristic = models.ForeignKey(Characteristics, models.DO_NOTHING, db_column='CharacteristicID', blank=True, null=True)
#     partscostmin = models.DecimalField(db_column='PartsCostMin', max_digits=10, decimal_places=4)
#
#     class Meta:
#         managed = False
#         db_table = 'PlatingSupplier'
#
# @python_2_unicode_compatible
# class Platingsupplierprice(models.Model):
#     platingsupplierprice = models.AutoField(db_column='PlatingSupplierPriceID', primary_key=True)
#     platingsupplier = models.ForeignKey(Platingsupplier, models.DO_NOTHING, db_column='PlatingSupplierID')
#     threaddiameterinchequivalentmin = models.DecimalField(db_column='ThreadDiameterInchEquivalentMin', max_digits=6, decimal_places=4)
#     threaddiameterinchequivalentmax = models.DecimalField(db_column='ThreadDiameterInchEquivalentMax', max_digits=6, decimal_places=4)
#     weightmax = models.IntegerField(db_column='WeightMax')
#     priceper100lb = models.DecimalField(db_column='PricePer100Lb', max_digits=10, decimal_places=4)
#
#     class Meta:
#         managed = False
#         db_table = 'PlatingSupplierPrice'
#
# @python_2_unicode_compatible
# class Processeffort(models.Model):
#     processeffort = models.AutoField(db_column='ProcessEffortID', primary_key=True)
#     processtype = models.ForeignKey('Processtype', models.DO_NOTHING, db_column='ProcessTypeID')
#     processoperationtype = models.ForeignKey('Processoperationtype', models.DO_NOTHING, db_column='ProcessOperationTypeID')
#     threaddiameterinchequivalentmin = models.DecimalField(db_column='ThreadDiameterInchEquivalentMin', max_digits=6, decimal_places=4)
#     threaddiameterinchequivalentmax = models.DecimalField(db_column='ThreadDiameterInchEquivalentMax', max_digits=6, decimal_places=4)
#     setuphours = models.DecimalField(db_column='SetupHours', max_digits=4, decimal_places=2)
#     perpiecehours = models.DecimalField(db_column='PerPieceHours', max_digits=12, decimal_places=9)
#
#     class Meta:
#         managed = False
#         db_table = 'ProcessEffort'
#
# @python_2_unicode_compatible
# class Processoperationtype(models.Model):
#     processoperationtype = models.AutoField(db_column='ProcessOperationTypeID', primary_key=True)
#     name = models.CharField(db_column='Name', max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'ProcessOperationType'
#
# @python_2_unicode_compatible
# class Processrate(models.Model):
#     processrate = models.AutoField(db_column='ProcessRateID', primary_key=True)
#     processtype = models.ForeignKey('Processtype', models.DO_NOTHING, db_column='ProcessTypeID')
#     issetuprate = models.IntegerField(db_column='IsSetupRate')
#     rateamount = models.DecimalField(db_column='RateAmount', max_digits=10, decimal_places=4)
#
#     class Meta:
#         managed = False
#         db_table = 'ProcessRate'
#
# @python_2_unicode_compatible
# class Processtype(models.Model):
#     processtype = models.AutoField(db_column='ProcessTypeID', primary_key=True)
#     name = models.CharField(db_column='Name', max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'ProcessType'
#
# @python_2_unicode_compatible
# class Purchasepartspecfiles(models.Model):
#     purchasepartspec = models.CharField(db_column='PurchasePartSpecID', primary_key=True, max_length=10)
#     partnumber = models.ForeignKey(Partnumber, models.DO_NOTHING, db_column='PartNumberID')
#     characteristic = models.ForeignKey(Characteristics, models.DO_NOTHING, db_column='CharacteristicID', blank=True, null=True)
#     characteristicvalue = models.ForeignKey(Characteristicvalues, models.DO_NOTHING, db_column='CharacteristicValueID', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'PurchasePartSpecFiles'
#
# @python_2_unicode_compatible
# class Standard(models.Model):
#     standard = models.AutoField(db_column='StandardID', primary_key=True)
#     ischemistry = models.IntegerField(db_column='IsChemistry')
#     isthread = models.IntegerField(db_column='IsThread')
#     isdimentions = models.IntegerField(db_column='IsDimentions')
#     ismechanical = models.IntegerField(db_column='IsMechanical')
#     isplating = models.IntegerField(db_column='IsPlating')
#     ispackaging = models.IntegerField(db_column='IsPackaging')
#     measurementunit = models.ForeignKey(Measurementunit, models.DO_NOTHING, db_column='MeasurementUnitID')
#     documentname = models.CharField(db_column='DocumentName', max_length=50)
#     organization = models.ForeignKey(Organization, models.DO_NOTHING, db_column='OrganizationID')
#
#     class Meta:
#         managed = False
#         db_table = 'Standard'
#
# @python_2_unicode_compatible
# class Standard2Standard(models.Model):
#     standard = models.ForeignKey(Standard, models.DO_NOTHING, db_column='StandardID')
#     referencestandard = models.ForeignKey(Standard, models.DO_NOTHING, db_column='ReferenceStandardID')
#
#     class Meta:
#         managed = False
#         db_table = 'Standard2Standard'
#
# @python_2_unicode_compatible
# class Standard2Style(models.Model):
#     standard = models.ForeignKey(Standard, models.DO_NOTHING, db_column='StandardID')
#     style = models.ForeignKey('Style', models.DO_NOTHING, db_column='StyleID')
#
#     class Meta:
#         managed = False
#         db_table = 'Standard2Style'
#
# @python_2_unicode_compatible
# class Standard2Threaddiameter(models.Model):
#     standard = models.ForeignKey(Standard, models.DO_NOTHING, db_column='StandardID')
#     threaddiameter = models.ForeignKey('Threaddiameter', models.DO_NOTHING, db_column='ThreadDiameterID')
#     standard2threaddiameter = models.AutoField(db_column='Standard2ThreadDiameterID', primary_key=True)
#
#     class Meta:
#         managed = False
#         db_table = 'Standard2ThreadDiameter'
#
# @python_2_unicode_compatible
# class Standardspecchemistry(models.Model):
#     standardspecchemistry = models.IntegerField(db_column='StandardSpecChemistryID', primary_key=True)
#     standard2threaddiameter = models.ForeignKey(Standard2Threaddiameter, models.DO_NOTHING, db_column='Standard2ThreadDiameterID')
#     standard = models.ForeignKey(Standard, models.DO_NOTHING, db_column='StandardID')
#     pitch = models.ForeignKey(Pitch, models.DO_NOTHING, db_column='PitchID')
#     designation = models.ForeignKey(Designation, models.DO_NOTHING, db_column='DesignationID')
#     style = models.ForeignKey('Style', models.DO_NOTHING, db_column='StyleID')
#     characteristicvalues = models.ForeignKey(Characteristicvalues, models.DO_NOTHING, db_column='CharacteristicValuesID', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'StandardSpecChemistry'
#
# @python_2_unicode_compatible
# class Standardspecdimensional(models.Model):
#     standard2threaddiameter = models.ForeignKey(Standard2Threaddiameter, models.DO_NOTHING, db_column='Standard2ThreadDiameterID')
#     standard = models.ForeignKey(Standard, models.DO_NOTHING, db_column='StandardID')
#     standardspecdimentional = models.AutoField(db_column='StandardSpecDimentionalID', primary_key=True)
#     style = models.ForeignKey('Style', models.DO_NOTHING, db_column='StyleID')
#     designation = models.ForeignKey(Designation, models.DO_NOTHING, db_column='DesignationID')
#     datadimentional = models.ForeignKey(Datadimentional, models.DO_NOTHING, db_column='DataDimentionalID')
#
#     class Meta:
#         managed = False
#         db_table = 'StandardSpecDimensional'
#
# @python_2_unicode_compatible
# class Standardspecmechanicperformance(models.Model):
#     standardspecmechanicperformance = models.IntegerField(db_column='StandardSpecMechanicPerformanceID', primary_key=True)
#     standard2threaddiameter = models.ForeignKey(Standard2Threaddiameter, models.DO_NOTHING, db_column='Standard2ThreadDiameterID')
#     standard = models.ForeignKey(Standard, models.DO_NOTHING, db_column='StandardID')
#     pitch = models.ForeignKey(Pitch, models.DO_NOTHING, db_column='PitchID')
#     designation = models.ForeignKey(Designation, models.DO_NOTHING, db_column='DesignationID')
#     style = models.ForeignKey('Style', models.DO_NOTHING, db_column='StyleID')
#     characteristicvalues = models.ForeignKey(Characteristicvalues, models.DO_NOTHING, db_column='CharacteristicValuesID', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'StandardSpecMechanicPerformance'
#
# @python_2_unicode_compatible
# class Standardspecpackaging(models.Model):
#     standardspecpackaging = models.IntegerField(db_column='StandardSpecPackagingID', primary_key=True)
#     standard = models.ForeignKey(Standard, models.DO_NOTHING, db_column='StandardID')
#     datapackaging = models.ForeignKey(Datapackaging, models.DO_NOTHING, db_column='DataPackagingID')
#
#     class Meta:
#         managed = False
#         db_table = 'StandardSpecPackaging'
#
# @python_2_unicode_compatible
# class Standardspecplating(models.Model):
#     standard = models.ForeignKey(Standard, models.DO_NOTHING, db_column='StandardID')
#     standardspecplating = models.AutoField(db_column='StandardSpecPlatingID', primary_key=True)
#     pointer = models.CharField(db_column='Pointer', max_length=10, blank=True, null=True)
#     characteristicvalue = models.ForeignKey(Characteristicvalues, models.DO_NOTHING, db_column='CharacteristicValueID', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'StandardSpecPlating'
#
# @python_2_unicode_compatible
# class Standardspecthreadinspection(models.Model):
#     standardspecthreadinspection = models.IntegerField(db_column='StandardSpecThreadInspectionID', primary_key=True)
#     standard = models.ForeignKey(Standard, models.DO_NOTHING, db_column='StandardID')
#     pitch2threaddiameter = models.ForeignKey(Pitch2Threaddiameter, models.DO_NOTHING, db_column='Pitch2ThreadDiameterID')
#     datathreadinspection = models.ForeignKey(Datathreadinspection, models.DO_NOTHING, db_column='DataThreadInspectionID')
#
#     class Meta:
#         managed = False
#         db_table = 'StandardSpecThreadInspection'
#
# @python_2_unicode_compatible
# class Standardspecthreadtolerance(models.Model):
#     standardspecthreadtolerance = models.IntegerField(db_column='StandardSpecThreadToleranceID', primary_key=True)
#     standard = models.ForeignKey(Standard, models.DO_NOTHING, db_column='StandardID')
#     pitch2threaddiameter = models.ForeignKey(Pitch2Threaddiameter, models.DO_NOTHING, db_column='Pitch2ThreadDiameterID')
#     datathreadtolerance = models.ForeignKey(Datathreadtolerance, models.DO_NOTHING, db_column='DataThreadToleranceID')
#
#     class Meta:
#         managed = False
#         db_table = 'StandardSpecThreadTolerance'
#
# @python_2_unicode_compatible
# class Standardspectorqperformance(models.Model):
#     standardspectorqperformance = models.IntegerField(db_column='StandardSpecTorqPerformanceID', primary_key=True)
#     standard2threaddiameter = models.ForeignKey(Standard2Threaddiameter, models.DO_NOTHING, db_column='Standard2ThreadDiameterID')
#     standard = models.ForeignKey(Standard, models.DO_NOTHING, db_column='StandardID')
#     pitch = models.ForeignKey(Pitch, models.DO_NOTHING, db_column='PitchID')
#     characteristicvalues = models.ForeignKey(Characteristicvalues, models.DO_NOTHING, db_column='CharacteristicValuesID', blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'StandardSpecTorqPerformance'
#
# @python_2_unicode_compatible
# class Steel(models.Model):
#     steel = models.AutoField(db_column='SteelID', primary_key=True)
#     name = models.TextField(db_column='Name')
#
#     class Meta:
#         managed = False
#         db_table = 'Steel'
#
# @python_2_unicode_compatible
# class Style(models.Model):
#     style = models.IntegerField(db_column='StyleID', primary_key=True)
#     name = models.CharField(db_column='Name', max_length=50)
#
#     class Meta:
#         managed = False
#         db_table = 'Style'

@python_2_unicode_compatible
class Threaddesignation(models.Model):
    # standard = models.ForeignKey(Standard, models.DO_NOTHING, db_column='StandardID')
    pitch2threaddiameter = models.ForeignKey(Pitch2Threaddiameter, models.DO_NOTHING, db_column='Pitch2ThreadDiameterID')
    threaddesignation = models.AutoField(db_column='ThreadDesignationID', primary_key=True)
    pitchthreaddiameterdesignation = models.ForeignKey(Pitchthreaddiameterdesignation, models.DO_NOTHING, db_column='PitchThreadDiameterDesignationID')

    class Meta:
        managed = False
        db_table = 'ThreadDesignation'

    def __str__(self):
        return


@python_2_unicode_compatible
class Threaddiameter(models.Model):
    threaddiameter = models.AutoField(db_column='ThreadDiameterID', primary_key=True)
    name = models.CharField(db_column='Name', unique=True, max_length=50)
    measurementunit = models.ForeignKey(Measurementunit, models.DO_NOTHING, db_column='MeasurementUnitID')
    inchmeasurementequivalent = models.DecimalField(db_column='InchMeasurementEquivalent', max_digits=16, decimal_places=4)

    class Meta:
        managed = False
        db_table = 'ThreadDiameter'

    def __str__(self):
        return self.name
# @python_2_unicode_compatible
# class Threadtoleranceclass(models.Model):
#     threadtoleranceclass = models.IntegerField(db_column='ThreadToleranceClassID', primary_key=True)
#     threadtolerancedeviationtype = models.ForeignKey('Threadtolerancedeviationtype', models.DO_NOTHING, db_column='ThreadToleranceDeviationTypeID')
#     threadtolerancegrade = models.ForeignKey('Threadtolerancegrade', models.DO_NOTHING, db_column='ThreadToleranceGradeID')
#
#     class Meta:
#         managed = False
#         db_table = 'ThreadToleranceClass'
#
# @python_2_unicode_compatible
# class Threadtolerancedeviationtype(models.Model):
#     threadtolerancedeviationtype = models.IntegerField(db_column='ThreadToleranceDeviationTypeID', primary_key=True)
#     name = models.CharField(db_column='Name', max_length=10)
#
#     class Meta:
#         managed = False
#         db_table = 'ThreadToleranceDeviationType'
#
# @python_2_unicode_compatible
# class Threadtolerancegrade(models.Model):
#     threadtolerancegrade = models.IntegerField(db_column='ThreadToleranceGradeID', primary_key=True)
#     name = models.CharField(db_column='Name', max_length=10, blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'ThreadToleranceGrade'
#
# @python_2_unicode_compatible
# class Torquetf(models.Model):
#     torquetf = models.AutoField(db_column='TorqueTFID', primary_key=True)
#     name = models.TextField(db_column='Name')
#
#     class Meta:
#         managed = False
#         db_table = 'TorqueTF'
#
# @python_2_unicode_compatible
# class AuthGroup(models.Model):
#     name = models.CharField(unique=True, max_length=80)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group'
#
# @python_2_unicode_compatible
# class AuthGroupPermissions(models.Model):
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#     permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_group_permissions'
#         unique_together = (('group', 'permission'),)
#
# @python_2_unicode_compatible
# class AuthPermission(models.Model):
#     name = models.CharField(max_length=255)
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
#     codename = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_permission'
#         unique_together = (('content_type', 'codename'),)
#
# @python_2_unicode_compatible
# class AuthUser(models.Model):
#     password = models.CharField(max_length=128)
#     last_login = models.DateTimeField(blank=True, null=True)
#     is_superuser = models.IntegerField()
#     username = models.CharField(unique=True, max_length=150)
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     email = models.CharField(max_length=254)
#     is_staff = models.IntegerField()
#     is_active = models.IntegerField()
#     date_joined = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user'
#
# @python_2_unicode_compatible
# class AuthUserGroups(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_groups'
#         unique_together = (('user', 'group'),)
#
# @python_2_unicode_compatible
# class AuthUserUserPermissions(models.Model):
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#     permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'auth_user_user_permissions'
#         unique_together = (('user', 'permission'),)
#
# @python_2_unicode_compatible
# class DjangoAdminLog(models.Model):
#     action_time = models.DateTimeField()
#     object_ = models.TextField(blank=True, null=True)
#     object_repr = models.CharField(max_length=200)
#     action_flag = models.SmallIntegerField()
#     change_message = models.TextField()
#     content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
#     user = models.ForeignKey(AuthUser, models.DO_NOTHING)
#
#     class Meta:
#         managed = False
#         db_table = 'django_admin_log'
#
# @python_2_unicode_compatible
# class DjangoContentType(models.Model):
#     app_label = models.CharField(max_length=100)
#     model = models.CharField(max_length=100)
#
#     class Meta:
#         managed = False
#         db_table = 'django_content_type'
#         unique_together = (('app_label', 'model'),)
#
# @python_2_unicode_compatible
# class DjangoMigrations(models.Model):
#     app = models.CharField(max_length=255)
#     name = models.CharField(max_length=255)
#     applied = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_migrations'
#
# @python_2_unicode_compatible
# class DjangoSession(models.Model):
#     session_key = models.CharField(primary_key=True, max_length=40)
#     session_data = models.TextField()
#     expire_date = models.DateTimeField()
#
#     class Meta:
#         managed = False
#         db_table = 'django_session'
#
# @python_2_unicode_compatible
# class Sysdiagrams(models.Model):
#     name = models.CharField(max_length=160)
#     principal_ = models.IntegerField()
#     diagram_ = models.AutoField(primary_key=True)
#     version = models.IntegerField(blank=True, null=True)
#     definition = models.TextField(blank=True, null=True)
#
#     class Meta:
#         managed = False
#         db_table = 'sysdiagrams'
#         unique_together = (('principal_id', 'name'),)

# from django.db import models
#
#
# class AlignedSalesFile(models.Model):
#     geography_id = models.IntegerField()
#     geography_name = models.CharField(max_length=100)
#     sales_crediting_product = models.CharField(max_length=100)
#     sales_crediting_country = models.CharField(max_length=100)
#     sales_crediting_metric = models.CharField(max_length=100)
#     sales_channel = models.CharField(max_length=100)
#     sales_crediting_channel_source = models.CharField(max_length=100)
#     prd_cm_1 = models.CharField(max_length=100)
#     prd_cm_2 = models.CharField(max_length=100)
#     prd_cm_3 = models.CharField(max_length=100)
#     prd_cm_4 = models.CharField(max_length=100)
#     prd_cm_5 = models.CharField(max_length=100)
#     prd_cm_6 = models.CharField(max_length=100)
#     prd_cm_7 = models.CharField(max_length=100)
#     prd_cm_8 = models.CharField(max_length=100)
#     prd_cm_9 = models.CharField(max_length=100)
#     prd_cm_10 = models.CharField(max_length=100)
#     prd_cm_11 = models.CharField(max_length=100)
#     prd_cm_12 = models.CharField(max_length=100)
#     prd_cm_13 = models.CharField(max_length=100)
#     prd_cm_14 = models.CharField(max_length=100)
#     prd_cm_15 = models.CharField(max_length=100)
#     prd_cm_16 = models.CharField(max_length=100)
#     prd_cm_17 = models.CharField(max_length=100)
#     prd_cm_18 = models.CharField(max_length=100)
#     prd_cm_19 = models.CharField(max_length=100)
#     prd_cm_20 = models.CharField(max_length=100)
#     prd_cm_21 = models.CharField(max_length=100)
#     prd_cm_22 = models.CharField(max_length=100)
#     prd_cm_23 = models.CharField(max_length=100)
#     prd_cm_24 = models.CharField(max_length=100)
#     mkt_cm_1 = models.CharField(max_length=100)
#     mkt_cm_2 = models.CharField(max_length=100)
#     mkt_cm_3 = models.CharField(max_length=100)
#     mkt_cm_4 = models.CharField(max_length=100)
#     mkt_cm_5 = models.CharField(max_length=100)
#     mkt_cm_6 = models.CharField(max_length=100)
#
#
# class TerrProdFile(models.Model):
#     geography_id = models.IntegerField()
#     geography_name = models.CharField(max_length=100)
#     team_name = models.CharField(max_length=100)
#     role_id = models.CharField(max_length=100)
#     product = models.CharField(max_length=100)
#     channel = models.CharField(max_length=100)
#     current_month = models.IntegerField()
#     prd_so_1 = models.CharField(max_length=100)
#     prd_so_2 = models.CharField(max_length=100)
#     prd_so_3 = models.CharField(max_length=100)
#     prd_so_4 = models.CharField(max_length=100)
#     prd_so_5 = models.CharField(max_length=100)
#     prd_so_6 = models.CharField(max_length=100)
#     mkt_prd1_so1 = models.CharField(max_length=100)
#     mkt_prd1_so2 = models.CharField(max_length=100)
#     mkt_prd1_so3 = models.CharField(max_length=100)
#     mkt_prd1_so4 = models.CharField(max_length=100)
#     mkt_prd1_so5 = models.CharField(max_length=100)
#     mkt_prd1_so6 = models.CharField(max_length=100)
#     curr_prd_sls = models.CharField(max_length=100)
#     curr_prd1_mkt_sls = models.CharField(max_length=100)
#     bsl_prd_sls = models.CharField(max_length=100)
#     bsl_mkt_sls = models.CharField(max_length=100)
#     prd1_ptd_mkt_shr = models.CharField(max_length=100)
#     bsl_prd1_mkt_shr = models.CharField(max_length=100)
#     prd1_curr_shr_chg = models.CharField(max_length=100)
#     prd1_share_weight = models.CharField(max_length=100)
#
#
# class BaseLineProduct(models.Model):
#     geography_id = models.IntegerField()
#     geography_name = models.CharField(max_length=100)
#     sales_crediting_product = models.CharField(max_length=100)
#     sales_crediting_country = models.CharField(max_length=100)
#     sales_crediting_metric = models.CharField(max_length=100)
#     sales_channel = models.CharField(max_length=100)
#     sales_crediting_channel_source = models.CharField(max_length=100)
#     total_business_sale = models.CharField(max_length=100)
#     base_month_1 = models.IntegerField()
#     base_month_2 = models.IntegerField()
#     base_month_3 = models.IntegerField()
#     base_month_4 = models.IntegerField()
#     base_month_5 = models.IntegerField()
#
#
# class Heirarchy(models.Model):
#     terr_id = models.IntegerField()
#     sale_force_id = models.IntegerField()
#     terr_name = models.CharField(max_length=100)
#     team_id = models.IntegerField()
#     team_name = models.CharField(max_length=100)
#     level_id = models.IntegerField()
#     partner_terr_id = models.IntegerField()
#     pod_id = models.IntegerField()
#     dist_id = models.IntegerField()
#     region_id_p = models.IntegerField()
#
#
# class MirrorGeographyMapping(models.Model):
#     geography_id = models.IntegerField()
#     geography_name = models.CharField(max_length=100)
#     mirror_terr_id = models.IntegerField()
#     mirror_terr_id_name = models.CharField(max_length=100)
#     mirror_base_mapping_flag = models.BooleanField()
#
#
# class ProductMetricWeightChange(models.Model):
#     geography_id = models.IntegerField()
#     geography_name = models.CharField(max_length=100)
#     bu_id = models.IntegerField()
#     sale_force_id = models.IntegerField()
#     sale_force_name = models.CharField(max_length=100)
#     product_id = models.IntegerField()
#     product_name = models.CharField(max_length=100)
#
#
# class AlignEligibility(models.Model):
#     geography_id = models.IntegerField()
#     geography_name = models.CharField(max_length=100)
#     employee_id = models.IntegerField()
#     employee_name = models.CharField(max_length=100)
#     designation = models.CharField(max_length=100)
#     bu_id = models.IntegerField()
#     hire_date = models.DateTimeField()
#     position_start_date = models.DateTimeField()
#     original_position_start_date = models.DateTimeField()
#     position_status_loa = models.CharField(max_length=100)
#     start_date_loa = models.CharField(max_length=100)
#     end_termination_date = models.DateTimeField()
#     nhp_start = models.CharField(max_length=100)
#     nhp_end = models.CharField(max_length=100)
#     nhp_eligible = models.BooleanField()
#     ic_eligibility_old_reps = models.CharField(max_length=100)
#     nhp_eligible_flag = models.BooleanField()
#
#
# class PaycurveRank(models.Model):
#     geography_id = models.IntegerField()
#     geography_name = models.CharField(max_length=100)
#     bu_name = models.IntegerField()
#     team_id = models.IntegerField()
#     team_name = models.CharField(max_length=100)
#     role_id = models.IntegerField()
#     geo_level_name = models.CharField(max_length=100)
#     rank = models.CharField(max_length=100)
#
#
# class PaycurveAttainment(models.Model):
#     pass
#
#
# class PayGrade(models.Model):
#     bu_name = models.IntegerField()
#     team_id = models.IntegerField()
#     team_name = models.CharField(max_length=100)
#     role_id = models.IntegerField()
#     level = models.CharField(max_length=100)
#     rank = models.CharField(max_length=100)
#     pay_grade_id = models.IntegerField()
#     annual_target_pay = models.IntegerField()
#
#
# class MasterDataSet(models.Model):
#     pass


from django.db import models


class Geography(models.Model):
    geography_id = models.IntegerField(primary_key=True)
    geography_name = models.CharField(max_length=100)

    def __str__(self):
        return self.geography_name


class Product(models.Model):
    product_name = models.CharField(max_length=100)

    def __str__(self):
        return self.product_name


class SalesChannel(models.Model):
    channel_name = models.CharField(max_length=100)

    def __str__(self):
        return self.channel_name


class Team(models.Model):
    team_name = models.CharField(max_length=100)

    def __str__(self):
        return self.team_name


class AlignedSalesFile(models.Model):
    geography = models.ForeignKey(Geography, on_delete=models.CASCADE)
    sales_crediting_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sales_crediting_country = models.CharField(max_length=100)
    sales_crediting_metric = models.CharField(max_length=100)
    sales_channel = models.ForeignKey(SalesChannel, on_delete=models.CASCADE)
    sales_crediting_channel_source = models.CharField(max_length=100)

    # Product metrics fields
    prd_cm = models.JSONField(default=dict)  # Using JSON to store the various prd_cm fields

    # Marketing metrics fields
    mkt_cm = models.JSONField(default=dict)  # Using JSON to store the various mkt_cm fields


class TerrProdFile(models.Model):
    geography = models.ForeignKey(Geography, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    role_id = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    channel = models.ForeignKey(SalesChannel, on_delete=models.CASCADE)
    current_month = models.IntegerField()

    # Product sales fields
    prd_so = models.JSONField(default=dict)  # Using JSON to store various prd_so fields
    mkt_prd1_so = models.JSONField(default=dict)  # Using JSON to store various marketing fields

    # Current and baseline sales
    curr_prd_sls = models.CharField(max_length=100)
    bsl_prd_sls = models.CharField(max_length=100)


class BaseLineProduct(models.Model):
    geography = models.ForeignKey(Geography, on_delete=models.CASCADE)
    sales_crediting_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sales_crediting_country = models.CharField(max_length=100)
    sales_crediting_metric = models.CharField(max_length=100)
    sales_channel = models.ForeignKey(SalesChannel, on_delete=models.CASCADE)
    total_business_sale = models.CharField(max_length=100)

    base_months = models.JSONField(default=dict)  # Using JSON to store base month data


class Hierarchy(models.Model):
    terr_id = models.IntegerField()
    sale_force_id = models.IntegerField()
    terr_name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    level_id = models.IntegerField()
    partner_terr_id = models.IntegerField()
    pod_id = models.IntegerField()
    dist_id = models.IntegerField()
    region_id_p = models.IntegerField()


class MirrorGeographyMapping(models.Model):
    geography = models.ForeignKey(Geography, on_delete=models.CASCADE)
    mirror_terr_id = models.IntegerField()
    mirror_terr_id_name = models.CharField(max_length=100)
    mirror_base_mapping_flag = models.BooleanField()


class ProductMetricWeightChange(models.Model):
    geography = models.ForeignKey(Geography, on_delete=models.CASCADE)
    bu_id = models.IntegerField()
    sale_force_id = models.IntegerField()
    sale_force_name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class AlignEligibility(models.Model):
    geography = models.ForeignKey(Geography, on_delete=models.CASCADE)
    employee_id = models.IntegerField()
    employee_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    bu_id = models.IntegerField()
    hire_date = models.DateTimeField()
    position_start_date = models.DateTimeField()
    original_position_start_date = models.DateTimeField()
    position_status_loa = models.CharField(max_length=100)
    start_date_loa = models.CharField(max_length=100)
    end_termination_date = models.DateTimeField()
    nhp_start = models.CharField(max_length=100)
    nhp_end = models.CharField(max_length=100)
    nhp_eligible = models.BooleanField()
    ic_eligibility_old_reps = models.CharField(max_length=100)
    nhp_eligible_flag = models.BooleanField()


class PaycurveRank(models.Model):
    geography = models.ForeignKey(Geography, on_delete=models.CASCADE)
    bu_name = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    role_id = models.IntegerField()
    geo_level_name = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)


class PayGrade(models.Model):
    bu_name = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    role_id = models.IntegerField()
    level = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    pay_grade_id = models.IntegerField()
    annual_target_pay = models.IntegerField()


class MasterDataSet(models.Model):
    # Define fields as needed
    pass

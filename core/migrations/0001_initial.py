from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Cliente')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome Completo')),
                ('cnpj', models.CharField(max_length=18, unique=True, verbose_name='CNPJ')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('endereco', models.TextField(verbose_name='Endereço Completo')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True, verbose_name='Data de Cadastro')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id_obra', models.AutoField(primary_key=True, serialize=False, verbose_name='ID Obra')),
                ('endereco_obra', models.CharField(max_length=200, verbose_name='Endereço da Obra')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('tempo_obra', models.CharField(max_length=50, verbose_name='Tempo Previsto')),
                ('data_inicio', models.DateField(verbose_name='Data de Início')),
                ('data_conclusao', models.DateField(blank=True, null=True, verbose_name='Data de Conclusão')),
                ('valor_obra', models.DecimalField(decimal_places=2, max_digits=12, verbose_name='Valor Total (R$)')),
                ('status_parcelado', models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=False, verbose_name='Status Parcelado')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição Detalhada')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente', verbose_name='Cliente Associado')),
            ],
            options={
                'verbose_name': 'Obra',
                'verbose_name_plural': 'Obras',
                'ordering': ['-data_inicio'],
            },
        ),
    ]
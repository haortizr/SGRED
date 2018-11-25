from django.conf.urls import url, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^accounts/login', auth_views.login, name='login'),
    url(r'^logout', auth_views.logout, name='logout'),

    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^proyecto', views.ver_proyecto, name='proyecto'),
    url('agregarCrudoBlock', views.upload_crudo_block, name='agregarCrudoBlock'),
    url('agregarCrudo', views.upload_crudo, name='agregarCrudo'),
    url('crudoDownload/(?P<crudoId>\d+)$', views.crudo_details_download, name='crudoDownload'),
    # sgrd 25 kata implementacion paso 2
    url('listaCrudos', views.crudo_list, name='listaCrudos'),
    url(r'^proyecto', views.ver_proyecto, name='proyecto'),
    url(r'^planLogistica/(?P<planId>\d+)$', views.get_plan_logistica, name='plan_logistica'),
    url(r'^planLogistica/(?P<planId>\d+)/actividades/$', views.get_actividades, name='actividades'),
    url(r'^planLogistica/(?P<planId>\d+)/actividad/(?P<actId>\d+)$', views.add_actividad, name='agregarActividad'),
    url(r'^planLogistica/(?P<planId>\d+)/actividad/$', views.add_actividad, name='agregarActividad'),
    url(r'editarActividad/(?P<id>\d+)$', views.edit_actividad, name='editarActividad'),
    url(r'^etapas/$', views.etapa_list),
    url(r'^actividades/$', views.actividades_view),
    url(r'^etapas/(?P<pk>[0-9]+)/$', views.etapa_detail),
    url(r'^solicitudesCambio/$', views.solicitud_cambio_estado_list),
    url(r'^solicitudesCambio/(?P<pk>[0-9]+)/$', views.solicitud_cambio_estado_detail),
    url(r'^cambioEstadoEtapa/(?P<pk>[0-9]+)/$', views.cambioEstadoEtapa, name='cambioEstadoEtapa'),
    url(r'^avanzarEtapa/(?P<pk>[0-9]+)/solicitud/(?P<pk2>[0-9]+)$', views.realizarAvanceEtapa),
    url(r'^getNotifications/$', views.getNotifications),
    url(r'^crearRecurso/$', views.crear_Recurso, name='crearRecurso'),
    url(r'^static-tables/$', views.static_tables, name='static-tables'),
    url(r'^agregarArtefactoRecurso/$', views.agregarArtefactoRecurso, name='agregarArtefactoRecurso'),
    url(r'^agregarPlanLogistica/$', views.agregarPlanLogistica, name='agregarPlanLogistica'),

    url('verSolicitudes', views.solicitudes_list, name='verSolicitudes'),
    url('recursosAsociados', views.getViewRecursosAsignados, name='verRecursosAsociados'),

    url(r'^checkActividad/(?P<id>\d+)$', views.checkActividad, name='checkActividad'),

    url('entregablesRecurso', views.RecursosList.as_view(), name='entregablesRecurso'),
    url(r'^detalleEntregablesRecurso/(?P<recursoId>\d+)/$', views.entregablesRecursos, name='detalleEntregablesRecurso'),

    url(r'^SolicitudControlCalidad/', views.SolicitudControlCalidad, name='SolicitudControlCalidad'),
    url(r'^listSolicitudControlCalidad/', views.ListarSolicitudesControlCalidad, name='listSolicitudControlCalidad'),
    url(r'ListaControlCalidad/(?P<filtro>\w+)/$', views.ListaControlCalidad, name='ListaControlCalidadFiltrado'),
    url('ListaControlCalidad/', views.ListaControlCalidad, name='ListaControlCalidadCompleto')
]

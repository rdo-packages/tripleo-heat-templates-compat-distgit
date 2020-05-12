# guard for package OSP does not support
%global rhosp 0

%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
%define upstream_name tripleo-heat-templates
%define old_version_name rocky

Name:          openstack-%{upstream_name}-compat
Summary:       Heat templates for TripleO old version support
Version:       XXX
Release:       XXX
License:       ASL 2.0
Group:         System Environment/Base
URL:           https://wiki.openstack.org/wiki/TripleO
Source0:       https://tarballs.openstack.org/tripleo-heat-templates/tripleo-heat-templates-%{upstream_version}.tar.gz

BuildArch:     noarch
BuildRequires: python3-devel
BuildRequires: python3-setuptools
BuildRequires: python3-pbr

BuildRequires: /usr/bin/pathfix.py

Requires:      ansible-pacemaker
Requires:      ansible-tripleo-ipsec
Requires:      ansible-role-container-registry
Requires:      python3-jinja2
Requires:      python3-six
Requires:      python3-paunch
Requires:      openstack-tripleo-common >= 7.1.0
Requires:      openstack-%{upstream_name}
%if 0%{rhosp} == 1
Requires:       ansible-role-redhat-subscription
%endif

Requires:      python3-PyYAML

%description
OpenStack TripleO Heat Templates is a collection of templates and tools for
building Heat Templates to do deployments of OpenStack.  These templates provide support for the clouds running the previous upstream version of OpenStack.

%prep
%setup -q -n tripleo-heat-templates-%{upstream_version}

%build
%{py3_build}

%install
%{py3_install}
install -d -m 755 %{buildroot}/%{_datadir}/openstack-%{upstream_name}/compat
cp -ar *.yaml %{buildroot}/%{_datadir}/openstack-%{upstream_name}/compat
cp -ar puppet %{buildroot}/%{_datadir}/openstack-%{upstream_name}/compat
cp -ar common %{buildroot}/%{_datadir}/openstack-%{upstream_name}/compat
if [ -d container_config_scripts ]; then
  cp -ar container_config_scripts %{buildroot}/%{_datadir}/openstack-%{upstream_name}/compat
fi
cp -ar firstboot %{buildroot}/%{_datadir}/openstack-%{upstream_name}/compat
cp -ar extraconfig %{buildroot}/%{_datadir}/openstack-%{upstream_name}/compat
cp -ar environments %{buildroot}/%{_datadir}/openstack-%{upstream_name}/compat
cp -ar network %{buildroot}/%{_datadir}/openstack-%{upstream_name}/compat
if [ -d networks ]; then
  cp -ar networks %{buildroot}/%{_datadir}/openstack-%{upstream_name}/compat
fi
cp -ar validation-scripts %{buildroot}/%{_datadir}/openstack-%{upstream_name}/compat
cp -ar deployed-server %{buildroot}/%{_datadir}/openstack-%{upstream_name}/compat
cp -ar ci %{buildroot}/%{_datadir}/openstack-%{upstream_name}/compat
cp -ar plan-samples %{buildroot}/%{_datadir}/openstack-%{upstream_name}/compat
cp -ar roles %{buildroot}/%{_datadir}/openstack-%{upstream_name}/compat
cp -ar scripts %{buildroot}/%{_datadir}/openstack-%{upstream_name}/compat
cp -ar tools %{buildroot}/%{_datadir}/openstack-%{upstream_name}/compat
if [ -d examples ]; then
  rm -rf examples
fi

if [ -d %{buildroot}/%{python3_sitelib}/tripleo_heat_merge ]; then
  rm -rf %{buildroot}/%{python3_sitelib}/tripleo_heat_merge
  rm -f %{buildroot}/%{_bindir}/tripleo-heat-merge
fi

ln -s compat %{buildroot}/%{_datadir}/openstack-%{upstream_name}/%{old_version_name}

# Fix shebangs for Python 3-only distros
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{_datadir}/openstack-%{upstream_name}/compat/container_config_scripts/*
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{_datadir}/openstack-%{upstream_name}/compat/extraconfig/post_deploy/*
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{_datadir}/openstack-%{upstream_name}/compat/tools/*
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{_datadir}/openstack-%{upstream_name}/compat/network/endpoints/*
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{_datadir}/openstack-%{upstream_name}/compat/scripts/*
pathfix.py -pni "%{__python3} %{py3_shbang_opts}" %{buildroot}%{_datadir}/openstack-%{upstream_name}/compat/common/*


%files
%doc README*
%license LICENSE
%{python3_sitelib}/tripleo_heat_templates-*.egg-info
%{_datadir}/openstack-%{upstream_name}/compat
%{_datadir}/openstack-%{upstream_name}/%{old_version_name}

%changelog

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
BuildRequires: python2-devel
BuildRequires: python2-setuptools
BuildRequires: python-d2to1
BuildRequires: python2-pbr

Requires:      PyYAML
Requires:      openstack-%{upstream_name}

%description
OpenStack TripleO Heat Templates is a collection of templates and tools for
building Heat Templates to do deployments of OpenStack.  These templates provide support for the clouds running the previous upstream version of OpenStack.

%prep
%setup -q -n tripleo-heat-templates-%{upstream_version}

%build
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}

%install
install -d -m 755 %{buildroot}/%{_datadir}/%{name}/compat
cp -ar *.yaml %{buildroot}/%{_datadir}/%{name}/compat
cp -ar puppet %{buildroot}/%{_datadir}/%{name}/compat
cp -ar common %{buildroot}/%{_datadir}/%{name}/compat
cp -ar docker %{buildroot}/%{_datadir}/%{name}/compat
if [ -d docker_config_scripts ]; then
  cp -ar docker_config_scripts %{buildroot}/%{_datadir}/%{name}/compat
fi
cp -ar firstboot %{buildroot}/%{_datadir}/%{name}/compat
cp -ar extraconfig %{buildroot}/%{_datadir}/%{name}/compat
cp -ar environments %{buildroot}/%{_datadir}/%{name}/compat
cp -ar network %{buildroot}/%{_datadir}/%{name}/compat
if [ -d networks ]; then
  cp -ar networks %{buildroot}/%{_datadir}/%{name}/compat
fi
cp -ar validation-scripts %{buildroot}/%{_datadir}/%{name}/compat
cp -ar deployed-server %{buildroot}/%{_datadir}/%{name}/compat
cp -ar ci %{buildroot}/%{_datadir}/%{name}/compat
cp -ar plan-samples %{buildroot}/%{_datadir}/%{name}/compat
cp -ar roles %{buildroot}/%{_datadir}/%{name}/compat
cp -ar scripts %{buildroot}/%{_datadir}/%{name}/compat
cp -ar tools %{buildroot}/%{_datadir}/%{name}/compat
if [ -d examples ]; then
  rm -rf examples
fi

if [ -d %{buildroot}/%{python2_sitelib}/tripleo_heat_merge ]; then
  rm -rf %{buildroot}/%{python2_sitelib}/tripleo_heat_merge
  rm -f %{buildroot}/%{_bindir}/tripleo-heat-merge
fi

ln -s compat %{buildroot}/%{_datadir}/openstack-%{upstream_name}/%{old_version_name}

%files
%doc README*
%license LICENSE
%{python2_sitelib}/tripleo_heat_templates-*.egg-info
%{_datadir}/openstack-%{upstream_name}/compat
%{_datadir}/openstack-%{upstream_name}/%{old_version_name}

%changelog

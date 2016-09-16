%define upstream_name tripleo-heat-templates

Name:		openstack-%{upstream_name}-compat
Summary:	Heat templates for TripleO old version support
Version:    XXX
Release:    XXX
License:	ASL 2.0
Group:		System Environment/Base
URL:		https://wiki.openstack.org/wiki/TripleO
Source0:	http://tarballs.openstack.org/tripleo-heat-templates/tripleo-heat-templates-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	python2-devel
BuildRequires:	python-setuptools
BuildRequires:	python-d2to1
BuildRequires:	python-pbr

Requires:	PyYAML
Requires:   openstack-%{upstream_name}

%description
OpenStack TripleO Heat Templates is a collection of templates and tools for
building Heat Templates to do deployments of OpenStack.  These templates provide support for the clouds running the previous upstream version of OpenStack.

%prep
%setup -q -n tripleo-heat-templates-%{upstream_version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install -O1 --skip-build --root=%{buildroot}
install -d -m 755 %{buildroot}/%{_datadir}/%{name}/compat
cp -ar *.yaml %{buildroot}/%{_datadir}/%{name}/compat
cp -ar puppet %{buildroot}/%{_datadir}/%{name}/compat
cp -ar docker %{buildroot}/%{_datadir}/%{name}/compat
cp -ar firstboot %{buildroot}/%{_datadir}/%{name}/compat
cp -ar extraconfig %{buildroot}/%{_datadir}/%{name}/compat
cp -ar environments %{buildroot}/%{_datadir}/%{name}/compat
cp -ar network %{buildroot}/%{_datadir}/%{name}/compat
cp -ar validation-scripts %{buildroot}/%{_datadir}/%{name}/compat
cp -ar deployed-server %{buildroot}/%{_datadir}/%{name}/compat
if [ -d examples ]; then
  rm -rf examples
fi

if [ -d %{buildroot}/%{python2_sitelib}/tripleo_heat_merge ]; then
  rm -rf %{buildroot}/%{python2_sitelib}/tripleo_heat_merge
  rm -f %{buildroot}/%{_bindir}/tripleo-heat-merge
fi

%files
%doc README*
%license LICENSE
%{python2_sitelib}/tripleo_heat_templates-*.egg-info
%{_datadir}/%{name}/compat

%changelog

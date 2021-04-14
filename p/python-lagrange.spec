%undefine _debugsource_packages
Name:           python-lagrange
Version:        20090327
Release:        5.1
License:        GPLv2
Summary:        Likelihood analysis of geographic range evolution
URL:            https://code.google.com/p/lagrange/
Group:          Development/Languages/Python
Source:         https://lagrange.googlecode.com/files/Lagrange-%{version}.tar.gz
BuildRequires:  python-devel
BuildArch:      noarch

%description
Lagrange is a Python package implementing likelihood models for geographic
range evolution on phylogenetic trees, with methods for inferring rates of
dispersal and local extinction and ancestral ranges.

%prep
%setup -q -n Lagrange-%{version}
sed -i '299,300s|as|s|' lagrange/decmodel_mp.py

%build

%install
mkdir -p %{buildroot}%{python2_sitelib}
cp -a lagrange %{buildroot}%{python2_sitelib}

%files
%{python2_sitelib}/lagrange

%changelog
* Sun May 05 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 20090327
- Rebuilt for Fedora

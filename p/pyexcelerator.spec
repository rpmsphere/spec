%undefine _debugsource_packages
Name:          pyexcelerator
Version:       0.6.4.1
Release:       4.1
Summary:       A module to work with Excel 97+ files
Group:         System/Libraries/Python
URL:           https://sourceforge.net/projects/pyexcelerator/
Source:        https://downloads.sourceforge.net/project/pyexcelerator/pyExcelerator/%{version}/%{name}-%{version}.zip
License:       BSD
BuildRequires: python-devel
Requires:      python
BuildArch:     noarch

%description
PyExcelerator generate Excel 97+ files, import Excel 95+ files, dump Excel and OLE2 files.

%prep
%setup -q

%build
python2 setup.py build

%install
rm -rf "$RPM_BUILD_ROOT"
python2 setup.py install \
   --root="$RPM_BUILD_ROOT" \
   --install-headers=%{_includedir}/python2.7 \
   --install-lib=%{python2_sitelib}

%files
%{python2_sitelib}/pyExcelerator-*.egg-info
%{python2_sitelib}/pyExcelerator

%changelog
* Mon Jun 20 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.4.1
- Rebuilt for Fedora
* Tue Jan 05 2010 Stefano Cotta Ramusino <stefano.cotta@openmamba.org> 0.6.4.1-1mamba
- package created by autospec

%global debug_package %{nil}
%define module_name dabo

Name: python-dabo
Version: 0.9.4
Release: 7.1
Summary: true 3-tier desktop application framework
License: BSD like
Url: http://dabodev.com/
Group: Development/Python
Source: http://dabodev.com/grabit/dabo/dabo-%{version}-mac-nix.tar.gz
BuildArch: noarch
BuildRequires: python
BuildRequires: python-setuptools

%description
Dabo is a Python module that provides a true 3-tier desktop application
framework. It separates the three main parts of a desktop app: database
access, user interface and business logic. You would typically use Dabo
to develop graphical, data-aware desktop applications.

%prep
%setup -q -n %module_name

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}
python2 setup.py install --root=$RPM_BUILD_ROOT --optimize=2
mv $RPM_BUILD_ROOT/usr/dabo/locale $RPM_BUILD_ROOT%{python2_sitelib}/dabo
rmdir $RPM_BUILD_ROOT/usr/dabo

%files
%doc AUTHORS ANNOUNCE ChangeLog dabo/LICENSE.TXT README TODO
%doc demo
%{python2_sitelib}/*

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%changelog
* Wed Jun 06 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.4
- Rebuild for Fedora
* Mon Dec 31 2007 Vitaly Lipatov <lav@altlinux.ru> 0.8.3-alt1
- initial build for ALT Linux Sisyphus

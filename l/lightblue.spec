Name:          lightblue
Version:       0.4
Release:       2.1
Summary:       Cross-platform Python Bluetooth library
Group:         System/Libraries/Python
URL:           http://lightblue.sourceforge.net
Source:        http://downloads.sourceforge.net/lightblue/lightblue-%{version}.tar.gz
License:       GPL
Requires:      python >= %python_version
BuildRequires: bluez-libs-devel
BuildRequires: openobex-devel
BuildRequires: python-devel
BuildRequires: pybluez
BuildRoot:     %{_tmppath}/%{name}-%{version}-root

%description
Cross-platform Python Bluetooth library for Mac OS X, GNU/Linux and Series 60.

%prep
%setup -q

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
   -O1 --skip-build \
   --root=$RPM_BUILD_ROOT \
   --install-headers=%{_includedir}/python \
   --install-lib=%{python_sitearch} \
   --record=%{name}.filelist

sed -i "\,\.egg-info/,d;s,.*/man/.*,&.gz," %{name}.filelist
mv doc html

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.filelist
%defattr(-,root,root)
%doc CHANGELOG COPYING README.txt html examples

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuilt for Fedora

* Mon Aug 23 2010 Stefano Cotta Ramusino <stefano.cotta@openmamba.org> 0.4-1mamba
- package created by autospec

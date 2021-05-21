Name:          python-wpactrl
Version:       20090609
Release:       2.1
Summary:       Python bindings for wpa_supplicant/hostapd ctrl socket
Group:         System/Libraries/Python
URL:           http://projects.otaku42.de/wiki/PythonWpaCtrl
Source:        http://mirror.leaseweb.com/software/archlinux/other/python-wpactrl/python-wpactrl-%{version}.tar.gz
License:       GPL
BuildRequires: python-devel
Requires:      python >= %python_version
BuildRoot:     %{_tmppath}/%{name}-%{version}-root

%description
wpactrl defines a single class, WPACtrl, that must be instantiated
with the pathname of a UNIX domain socket control interface of
a wpa_supplicant/hostapd daemon.

%prep
%setup -q

%build
CFLAGS="%{optflags}" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
   --root=$RPM_BUILD_ROOT \
   --install-headers=%{_includedir}/python \
   --install-lib=%{python_sitearch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{python_sitearch}/wpactrl.so
%{python_sitearch}/wpactrl-0.0.0-py*.egg-info

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 20090609
- Rebuilt for Fedora

* Sat Aug 01 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 20090609-1mamba
- package created by autospec

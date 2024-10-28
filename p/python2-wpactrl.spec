Name:          python2-wpactrl
Version:       20090609
Release:       2.1
Summary:       Python bindings for wpa_supplicant/hostapd ctrl socket
Group:         System/Libraries/Python
URL:           https://projects.otaku42.de/wiki/PythonWpaCtrl
Source:        https://mirror.leaseweb.com/software/archlinux/other/python-wpactrl/python-wpactrl-%{version}.tar.gz
License:       GPL
BuildRequires: python2-devel

%description
wpactrl defines a single class, WPACtrl, that must be instantiated
with the pathname of a UNIX domain socket control interface of
a wpa_supplicant/hostapd daemon.

%prep
%setup -q -n python-wpactrl-%{version}

%build
CFLAGS="%{optflags}" python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install \
   --root=$RPM_BUILD_ROOT \
   --install-headers=%{_includedir}/python2.7 \
   --install-lib=%{python2_sitearch}

%files
%{python2_sitearch}/wpactrl.so
%{python2_sitearch}/wpactrl-0.0.0-py*.egg-info

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 20090609
- Rebuilt for Fedora
* Sat Aug 01 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 20090609-1mamba
- package created by autospec

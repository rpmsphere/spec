Name:          python2-iwscan
Version:       20090609
Release:       4.1
Summary:       Python bindings for wireless scanning via iwlib
Group:         System/Libraries/Python
URL:           https://projects.otaku42.de/browser/python-iwscan
Source:        https://mirror.leaseweb.com/software/archlinux/other/python-iwscan/python-iwscan-%{version}.tar.gz
License:       GPL
BuildRequires: wireless-tools-devel
BuildRequires: python2-devel

%description
Python bindings for wireless scanning via iwlib.

%prep
%setup -q -n python-iwscan

%build
CFLAGS="%{optflags}" python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install \
   --root=$RPM_BUILD_ROOT \
   --install-headers=%{_includedir}/python2.7 \
   --install-lib=%{python2_sitearch}

%files
%{python2_sitearch}/iwscan.so
%{python2_sitearch}/iwscan-0.0.0-py*.egg-info

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 20090609
- Rebuilt for Fedora
* Sat Aug 01 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 20090609-1mamba
- package created by autospec

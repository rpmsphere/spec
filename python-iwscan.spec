Name:          python-iwscan
Version:       20090609
Release:       4.1
Summary:       Python bindings for wireless scanning via iwlib
Group:         System/Libraries/Python
URL:           http://projects.otaku42.de/browser/python-iwscan
Source:        http://mirror.leaseweb.com/software/archlinux/other/python-iwscan/python-iwscan-%{version}.tar.gz
License:       GPL
BuildRequires: wireless-tools-devel
BuildRequires: python-devel
BuildRoot:     %{_tmppath}/%{name}-%{version}-root

%description
Python bindings for wireless scanning via iwlib.

%prep
%setup -q -n %{name}

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
%{python_sitearch}/iwscan.so
%{python_sitearch}/iwscan-0.0.0-py*.egg-info

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 20090609
- Rebuild for Fedora

* Sat Aug 01 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 20090609-1mamba
- package created by autospec

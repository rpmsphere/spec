Summary:       A method of getting a CMYK TIFF out of GhostScript
Name:          bitcmyk2tiff
Version:       0.0.1
Release:       4.1
License:       GPL
Group:         Applications/Graphics
URL:           http://www.blackfiveservices.co.uk/bitcmyk2tiff.shtml
Source:        http://www.blackfiveservices.co.uk/projects/%{name}-%{version}.tar.gz
BuildRequires: gcc-c++
BuildRequires: libstdc++-devel
BuildRequires: libtiff-devel
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root

%description
It converts raw data from GhostScript's bitcmyk output device into a CMYK TIFF.

%prep
%setup -q

%build
%configure 
#--prefix=/usr --includedir=/usr/include
make 
#%{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_bindir}/*

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.1
- Rebuilt for Fedora

* Fri Jun 05 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 0.0.1-4mamba
- specfile updated

* Wed Jun 22 2005 Alessandro Ramazzina <alessandro.ramazzina@qilinux.it> 0.0.1-3qilnx
- modified package description

* Tue Jun 21 2005 Alessandro Ramazzina <alessandro.ramazzina@qilinux.it> 0.0.1-2qilnx
- rebuild and moved from devel-contrib repository to devel repository

* Mon Jun 20 2005 Matteo Bernasconi <voyagernm@virgilio.it> 0.0.1-1qilnx
- First Build

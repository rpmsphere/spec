%undefine _debugsource_packages
Summary:	Simplified object-oriented Python extension module for libpcap
Name:		python-pypcap
Version:	1.1
Release:	15.1
License:	BSD
Group:		Development/Python
URL:		http://monkey.org/~dugsong/pypcap/
Source0:	http://monkey.org/~dugsong/pypcap/pypcap-%{version}.tar.bz2
Patch0:		pypcap-1.1-lib64.diff
Patch1:     pypcap-1.1-fix_build.diff
BuildRequires:	python-devel
BuildRequires:	libpcap-devel

%description
Simplified object-oriented Python extension module for libpcap - 
the current tcpdump.org version, the legacy version shipping with
some of the BSD operating systems, and the WinPcap port for
Windows.

%prep
%setup -q -n pypcap-%{version}
%patch0 -p0
%patch1 -p0
sed -i -e 's|dylib|so|' -e "s|'include', 'include/pcap'|'include/pcap' , 'include'|" setup.py

%build
CFLAGS="%{optflags}" python2 setup.py config
CFLAGS="%{optflags}" python2 setup.py build

%install
rm -rf %{buildroot}
python2 setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%doc CHANGES LICENSE README

%changelog
* Sun May 05 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuilt for Fedora
* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 1.1-9mdv2011.0
+ Revision: 590001
- rebuild for python 2.7
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.1-8mdv2010.0
+ Revision: 442455
- rebuild
* Tue Mar 03 2009 Michael Scherer <misc@mandriva.org> 1.1-7mdv2009.1
+ Revision: 347777
- fix build ( and so rebuild )
  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt against libpcap-1.0.0
* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.1-5mdv2009.0
+ Revision: 259772
- rebuild
* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.1-4mdv2009.0
+ Revision: 247599
- rebuild
* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.1-2mdv2008.1
+ Revision: 136456
- restore BuildRoot
  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
* Wed Mar 21 2007 Michael Scherer <misc@mandriva.org> 1.1-2mdv2007.1
+ Revision: 147570
- Rebuild for new python
- Import python-pypcap
* Sun Mar 19 2006 Oden Eriksson <oeriksson@mandriva.com> 1.1-1mdk
- initial Mandriva package

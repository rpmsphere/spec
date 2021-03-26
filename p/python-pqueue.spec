%define module  PQueue

Summary: 	%{module} module for Python
Name: 		python-pqueue
Version: 	0.2
Release: 	1
License: 	LGPL
Group: 		Development/Python
Source: 	%{module}-%{version}.tar.bz2
Patch:		python-%{module}-0.2.lib64.patch
URL:		http://www.csse.monash.edu.au/hons/projects/1999/Andrew.Snare
BuildRequires:	python-devel
BuildRequires:	autoconf

%description 
This C extension implements a priority-queue object using a fibonacci
heap as the underlying data structure.

%prep
%setup -q -n %{module}
%patch -p 1

%build
autoconf
%configure
sed -i 's/BLDSHARED/LDSHARED/' Makefile
%__make

%install
rm -rf %{buildroot}
install -Dm 755 pqueuemodule.so %{buildroot}%{python_sitearch}/pqueuemodule.so

%clean 
rm -rf %{buildroot}

%files
%doc AUTHORS COPYING README
%{python_sitearch}/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuild for Fedora
* Fri Oct 31 2008 milochen <milo_chen@mail2000.com.tw> 0.2-8
- initial ossii package
* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.2-8mdv2008.1
+ Revision: 136456
- restore BuildRoot
  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
* Wed Dec 13 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.2-8mdv2007.0
+ Revision: 96530
- Rebuild against new python
- Import python-PQueue
* Wed Aug 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.2-7mdv2007.0
- Rebuild
* Wed Aug 24 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.2-6mdk
- fix x86_64 build 
- %%mkrel
- spec cleanup
* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 0.2-5mdk
- Rebuild for new python
* Thu Aug 05 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.2-4mdk 
- fixed perms

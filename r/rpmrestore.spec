Name:           rpmrestore
Version:        1.8
Release:        1
Summary:        Restores install attributes from the RPM database
Group:          System/Configuration/Packaging
License:        GPL
URL:            http://rpmrestore.sourceforge.net/
Source0:        http://ovh.dl.sourceforge.net/rpmrestore/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Pod::Usage)

%description
The RPM database stores the user, group, time, mode for all files,
and offers a command to display the changes between install state (database)
and current disk state. rpmrestore will help you to restore these install
attributes.

%prep
%setup -q

%build
make

%install
rm -rf %{buildroot}
%make_install
mv %{buildroot}%{_datadir}/doc/%{name}-%{version} %{buildroot}%{_datadir}/doc/%{name}

%clean
%{__rm} -rf %{buildroot}

%files
%{_datadir}/doc/%{name}
%{_bindir}/%{name}*
%{_mandir}/man1/%{name}*
%{_sysconfdir}/%{name}rc

%changelog
* Sun Sep 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8
- Rebuilt for Fedora
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 0:1.3-5mdv2010.0
+ Revision: 433455
- rebuild
* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 0:1.3-4mdv2009.0
+ Revision: 260335
- rebuild
* Mon Jul 28 2008 Thierry Vignaud <tvignaud@mandriva.com> 0:1.3-3mdv2009.0
+ Revision: 251499
- rebuild
- kill re-definition of %%buildroot on Pixel's request
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
* Fri Nov 16 2007 David Walluck <walluck@mandriva.org> 0:1.3-1mdv2008.1
+ Revision: 109030
- 1.3
* Thu Aug 16 2007 David Walluck <walluck@mandriva.org> 0:1.2-2mdv2008.0
+ Revision: 64096
- remove duplicate docs
- reflect the name that we install as
* Tue Mar 20 2007 David Walluck <walluck@mandriva.org> 1.2-1mdv2007.1
+ Revision: 147050
- 1.2
* Tue Jan 09 2007 David Walluck <walluck@mandriva.org> 0:1.1-1mdv2007.1
+ Revision: 106265
- 1.1
* Fri Dec 08 2006 David Walluck <walluck@mandriva.org> 0:1.0-1mdv2007.1
+ Revision: 92215
- 1.0
* Thu Nov 16 2006 David Walluck <walluck@mandriva.org> 0:0.9-1mdv2007.1
+ Revision: 84678
- 0.9
* Thu Nov 09 2006 David Walluck <walluck@mandriva.org> 0:0.8-1mdv2007.0
+ Revision: 79896
- 0.8
- 0.3
* Sun Oct 15 2006 David Walluck <walluck@mandriva.org> 0:0.1-1mdv2006.0
+ Revision: 64946
- Import rpmrestore
* Wed Oct 11 2006 David Walluck <walluck@mandriva.org> 0:0.1-1mdv2007.1
- release

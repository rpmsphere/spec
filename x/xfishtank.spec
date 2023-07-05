%undefine _debugsource_packages

Name:           xfishtank
BuildRequires:  libX11-devel, libXext-devel, imake, imlib2-devel
License:        GPLv2+
Group:          Amusements/Toys/Background
Version:        2.5
Release:        11.1
Summary:        An aquarium in the root window
Source:         %{name}-%{version}.tar.gz
URL:            https://jim.rees.org/computers/xfishtank.html

%description
A nice little aquarium with funny fish -- yet another background
screen.

%prep
%setup -q

%build
xmkmf -a
make %{?jobs:-j%jobs}

%install
make DESTDIR=$RPM_BUILD_ROOT MANPATH=%{_mandir} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc LICENSE README*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1x.*

%changelog
* Thu Aug 28 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5
- Rebuilt for Fedora
* Mon Nov  8 2010 coolo@novell.com
- remove support for pre-9.1
* Tue Aug  8 2006 lmichnovic@suse.cz
- compiling with RPM_OPT_FLAGS
- fixed non void functions (random_retval.patch)
* Fri Jul 28 2006 lmichnovic@suse.cz
- builds also with new X.org 7.x, detecting prefix in X.org
- building with icecream
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Mon Dec 19 2005 lmichnovic@suse.cz
- added missing include (implicit_decl.patch)
- repacked tarball: renamed xfishtank-2.2.orig to xfishtank-2.2, because ".orig" is not allowed string
* Sun Jan 11 2004 adrian@suse.de
- add %%defattr
* Tue Dec 18 2001 vinil@suse.cz
- README.KDE added
* Wed Jun 20 2001 ro@suse.de
- use ComplexProgramTargetNoMan
* Wed Nov 29 2000 vinil@suse.cz
- renamed from fishtank to xfishtank
- source bzip2ed
* Tue Jun 20 2000 schwab@suse.de
- Fix missing declarations.
* Thu May 25 2000 vinil@suse.cz
- sorted in group
* Fri Apr  7 2000 vinil@suse.cz
- buildroot added
* Mon Sep 13 1999 bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Wed Dec  9 1998 ro@suse.de
- update to 2.2 to fix segfault

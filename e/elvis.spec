%global docdir /usr/share/doc/elvis

Summary:	A clone of vi/ex
Name:		elvis
Release:	31.1
Version:	2.2.0
License:	Artistic (see LICENSE)
Group:		Applications/Editors
Vendor:     Steve Kirkendall <kirkenda@cs.pdx.edu>
URL:        http://elvis.vi-editor.org/
Source0:	ftp://ftp.cs.pdx.edu/pub/elvis/unreleased/%{name}-2.2_0.tar.gz
Patch0:     %{name}-2.2_0.patch
BuildRequires:  ncurses-devel libX11-devel libXt-devel
Patch1:     elvis.clr-Fedora.patch

%description
Elvis is a text editor, compatible with vi. It has all the usual
extensions (multiple buffers, multiple windows, syntax coloring,
etc.) plus a variety of display modes including "html" and "man".

Author:     Steve Kirkendall <kirkenda@cs.pdx.edu>

%prep
%setup -q -n %{name}-2.2_0
%patch0 -p0
%patch1 -p0

%build
export CFLAGS="$RPM_OPT_FLAGS" CPPFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS";
./configure --prefix=%{prefix} --libs="-lX11 -lncurses -lresolv"
make

%install
%{__mkdir_p} $RPM_BUILD_ROOT%{_bindir}
%{__mkdir_p} $RPM_BUILD_ROOT%{_mandir}/man1
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/%{name}/{icons,doc,scripts,stubs,themes}
%{__mkdir_p} $RPM_BUILD_ROOT%{docdir}
%{__mkdir_p} $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

install -m755 elvis $RPM_BUILD_ROOT%{_bindir}
install -m755 elvfmt $RPM_BUILD_ROOT%{_bindir}
install -m755 elvtags ref $RPM_BUILD_ROOT%{_bindir}
install -m755 ref $RPM_BUILD_ROOT%{_bindir}
install -m644 doc/elvis.man $RPM_BUILD_ROOT%{_mandir}/man1/elvis.1
install -m644 doc/ctags.man $RPM_BUILD_ROOT%{_mandir}/man1/elvtags.1
install -m644 doc/fmt.man $RPM_BUILD_ROOT%{_mandir}/man1/elvfmt.1
install -m644 doc/ref.man $RPM_BUILD_ROOT%{_mandir}/man1/ref.1
install -m644 data/elvis.* $RPM_BUILD_ROOT%{_sysconfdir}/%{name}

cp data/icons/*.xpm $RPM_BUILD_ROOT%{_datadir}/%{name}/icons
cp data/scripts/* $RPM_BUILD_ROOT%{_datadir}/%{name}/scripts
cp data/stubs/* $RPM_BUILD_ROOT%{_datadir}/%{name}/stubs
cp data/themes/* $RPM_BUILD_ROOT%{_datadir}/%{name}/themes
rm doc/*.man
cp doc/* $RPM_BUILD_ROOT%{docdir}
cp data/elvis.* $RPM_BUILD_ROOT%{docdir}
cp COPYING BUGS INSTALL README.html $RPM_BUILD_ROOT%{docdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{docdir}
%dir %{_datadir}/%{name}
%dir %{_sysconfdir}/%{name}
%{_bindir}/elvis
%{_bindir}/elvfmt
%{_bindir}/elvtags
%{_bindir}/ref
%{_mandir}/man1/*
%{_datadir}/%{name}/*
%{_sysconfdir}/%{name}/*

%changelog
* Wed Feb 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.0
- Rebuilt for Fedora
* Sat Jul 9 2011 Agnelo de la Crotche <agnelo@unixversal.com> - 
- added color patches for openSUSE, Fedora and Mandriva
* Fri Mar 18 2010 Agnelo de la Crotche <agnelo@unixversal.com> - 
- elvis is back in openSUSE. :-)

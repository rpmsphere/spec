%global debug_package %{nil}

Name:			tss
Version:		0.8.2
Release:		5.1
Summary:		VT Screen Saver
Source:			http://www.pulia.nu/tss/src/tss-%{version}.tar.gz
Patch1:			%{name}-makefile-flags.diff
Patch2:			%{name}-ascii-dir.diff
URL:			http://www.pulia.nu/tss/
Group:			System/Console
License:		GNU General Public License (GPL)
BuildRequires:	ncurses-devel glibc-devel make gcc

%description
Terminal ScreenSaver (or tss for short) is an attempt to clone and enhance
FreeBSD's text-mode screen saver. Although intended for GNU/Linux, it
works fine under FreeBSD and probably a lot of other Unix-based operating
systems. Unlike the daemonsaver in FreeBSD, you may choose ASCII art of your
own liking or make your own.

%prep
%setup -q
%patch1
%patch2

%build
%__make %{?jobs:-j%{jobs}} OPTFLAGS="%{optflags}" CC="%__cc"

%install
%__rm -rf "$RPM_BUILD_ROOT"
%__install -D -m 0755 tss "$RPM_BUILD_ROOT%{_bindir}/tss"
%__install -d "$RPM_BUILD_ROOT%{_datadir}/tss"
for x in tss_art/*; do
	%__install -m 0644 "$x" "$RPM_BUILD_ROOT%{_datadir}/tss/"
done

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%doc ART_CREDITS Changelog COPYING README
%{_bindir}/tss
%dir %{_datadir}/tss
%{_datadir}/tss/*

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.2
- Rebuild for Fedora
* Sat Dec 29 2007 Pascal Bleser <guru@unixtech.be> 0.8.1
- moved to openSUSE Build Service
- new upstream version
* Sun Mar 19 2006 Pascal Bleser <guru@unixtech.be> 0.8-1
- new package

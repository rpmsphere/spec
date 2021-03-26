Name: me-jasspa
Version: 161004
Release: 4.1
License: GPLv2
URL: http://www.jasspa.com/
Source0: jasspa-mesrc-%{version}.tar.gz
Source1: me.1
Summary: A much enhanced version of Daniel Lawrence's original MicroEmacs
Group: Applications/Editors
BuildRequires: cmake
BuildRequires: ncurses-devel

%description
JASSPA MicroEmacs is an enhanced version of Daniel Lawrence's original
MicroEmacs 3.8 of 1988. It has a small memory and disk footprint while still
providing most of the useful Emacs functionality. MicroEmacs includes X-window
support, an integrated spell-checker, macro language, major modes for most
languages, color syntax highlighting in X and console modes, online help, file
browser, and much more!

%prep
%setup -q -n me%{version}

%build
%cmake
make

%install
install -d -m 0755 %{buildroot}%{_bindir}
install -c -m 0755 src/me %{buildroot}%{_bindir}/me
install -d -m 0755 %{buildroot}%{_mandir}/man1
install -c -m 0644 %{SOURCE1} %{buildroot}%{_mandir}/man1

%clean
rm -rf %{buildroot}

%files
%doc ChangeLog README* COPYING *.txt
%{_bindir}/me
%{_mandir}/man1/me.1*

%changelog
* Fri Sep 15 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 20161004
- Rebuild for Fedora
* Mon Oct 12 2009 - Jon Green <support@jasspa.com>
- RPM package build for release 20091011

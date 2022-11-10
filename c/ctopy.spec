Summary: C to Python translator
Name: ctopy
Version: 1.4
Release: 1
License: BSD
Group: Development/Tools
URL: http://www.catb.org/~esr/ctopy/
Source: http://www.catb.org/~esr/ctopy/ctopy-%{version}.tar.gz
BuildArch: noarch

%description
ctopy automates the parts of translating C source code to Python
source code that are difficult for a human but easy for a
machine. This allows a human programmer to concentrate on the
nontrivial parts of the translation.

%prep 
%setup -q

%build

%install
%{__rm} -rf %{buildroot}
%{__install} -Dp -m0755 ctopy %{buildroot}%{_bindir}/ctopy
%{__install} -Dp -m0644 ctopy.1 %{buildroot}%{_mandir}/man1/ctopy.1

%clean
%{__rm} -rf %{buildroot}

%files
%doc COPYING README
%doc %{_mandir}/man1/ctopy.1*
%{_bindir}/ctopy

%changelog
* Sun Oct 23 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4
- Rebuilt for Fedora
* Tue Oct 26 2010 Dag Wieers <dag@wieers.com> - 1.1-1 - 9204/dag
- Updated to release 1.1.
* Sun Jan 21 2007 Dag Wieers <dag@wieers.com> - 1.0-2
- Fix group tag.
* Sat Oct 21 2006 Dag Wieers <dag@wieers.com> - 1.0-1
- Initial package. (using DAR)

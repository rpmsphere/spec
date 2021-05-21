Summary: A LaTeX to HTML converter
Name: tth
Version: 3.85
Release: 2.1
License: Free to use and redistribute.
Group: Applications/Text
URL: http://hutchinson.belmont.ma.us/tth/
Source: http://hutchinson.belmont.ma.us/tth/tth-noncom/tth_C.tgz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ghostscript, tetex-latex, tetex-dvips, netpbm-progs

%description
TTH is a very good LaTeX to HTML conversion program.

%prep
%setup -q -n tth_C

%build
gcc ${RPM_OPT_FLAGS} -o tth tth.c

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_mandir}/man1
cp latex2gif ps2gif ps2png tth %{buildroot}%{_bindir}
cp tth.1 %{buildroot}%{_mandir}/man1
ln -sf tth.1 %{buildroot}%{_mandir}/man1/ps2gif.1

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc license.txt tth_manual.html CHANGES tth.gif Xfonts.fix
%attr(0755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%changelog
* Mon Oct 14 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 3.85
- Rebuilt for Fedora

Name:           pstotext
Summary:        Extract plain text from PostScript
Version:        1.9
Release:        8.1
License:        DEC
URL:            http://pages.cs.wisc.edu/~ghost/doc/pstotext.htm
Group:          Productivity/Other
Source:         %{name}-%{version}.tar.bz2
Source1:        configure.ac
Source2:        Makefile.am
Patch:          pstotext-config_h.patch
Patch1:         pstotext-signed_unsigned_compare.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Pstotext extracts plain text from PostScript documents. It deals
successfully with a wide variety of encoding vectors, and it re-assembles
words that have been broken up for pair-kerning (it doesn't re-assemble
words that have been hyphenated, though). It also works (though a little
less reliably) on Acrobat PDF files.

%prep
%setup -q
%patch
%patch1
cp %{SOURCE1} %{SOURCE2} .
mv Makefile Makefile.original

%build
export SUSE_ASNEEDED=0
autoreconf -f -i
export CFLAGS="%{optflags} -W"
%configure
make %{?jobs:-j%jobs}

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc pstotext.txt
%{_bindir}/%{name}
%{_mandir}/man1/*

%changelog
* Sun Aug 05 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9
- Rebuild for Fedora
* Tue Jun 10 2008 pth@suse.de
- Initial package
- Create configure.ac and Makefile.am
- Fix comparisons of signed values with unsigned ones.

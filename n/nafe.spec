Name:           nafe
License:        GPL v2 or later
Group:          Development/Tools/Other
Summary:        Not Another Font Editor
URL:            https://nafe.sourceforge.net/
Version:        0.1
Release:        4.1
Source:         nafe-0.1.tar.gz
Patch1:         nafe-0.1-warnings.patch
Patch2:         nafe-0.1-rename.patch

%description
NAFE is no consolefont editor, but a toolset to translate psf format
consolefonts into text files and text files into psf files, The advantage is
that you can edit the font in the text file easily with any text editor (not
provided by nafe).  So you are independent from your actual terminal hardware
and don't need stuff like svgalib.

%prep
%setup -q
%patch 1
%patch 2

%build
make CFLAGS="$RPM_OPT_FLAGS" 

%install
install -d $RPM_BUILD_ROOT%{_bindir}
install -m755 txt2psf $RPM_BUILD_ROOT%{_bindir}/nafe-txt2psf
install -m755 psf2txt $RPM_BUILD_ROOT%{_bindir}/nafe-psf2txt

%files
%doc COPYING demo* readme.txt
%{_bindir}/*

%changelog
* Wed Jul 11 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora

* Wed Oct  1 2008 mmarek@suse.cz
- rename the toos to nafe-* to avoid conflict with psftools
* Tue Sep 30 2008 mmarek@suse.cz
- packaged nafe version 0.1

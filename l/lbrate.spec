Name:          lbrate
Version:       1.1
Release:       2
Summary:       Extracts files from CP/M archives in LBR format
License:       GPLv2
URL:           http://www.svgalib.org/rus/lbrate.html
Source0:       ftp://ftp.ibiblio.org/pub/Linux/utils/compress/lbrate-1.1.tar.gz
BuildRequires: gcc

%description
Extracts files from LBR archives which was a common format on the CP/M
operating system. It supports all LBR compression schemes (Q, Z, Y)

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="${CFLAGS}" PREFIX="%{_prefix}"

%install
mkdir -p %{buildroot}%{_bindir} \
         %{buildroot}%{_mandir}/man1
install -pm 0755 lbrate %{buildroot}%{_bindir}
install -pm 0644 lbrate.1 %{buildroot}%{_mandir}/man1

%files
%doc ChangeLog NEWS README TODO
%license COPYING lzhuf-post.txt
%{_bindir}/%{name}
%{_mandir}/man1/lbrate.1*

%changelog
* Sun Nov 27 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuilt for Fedora
* Sun Dec 27 2020 RPM Builder - 1.1-2
- Minor SPEC cleanups
* Mon Nov 12 2018 RPM Builder - 1.1-1
- Initial RPM

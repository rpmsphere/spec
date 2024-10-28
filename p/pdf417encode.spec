%undefine _debugsource_packages

Summary:       Converts ascii text to the pdf417 barcode standard
Name:          pdf417encode
Version:       4.5
Release:       4.1
License:       GPL
Group:         Applications/Graphics
URL:           https://sourceforge.net/projects/pdf417encode/
Source0:       https://switch.dl.sourceforge.net/sourceforge/pdf417encode/pdf417_enc.%{version}.tar.gz
BuildRequires: glibc-devel
BuildRequires: giflib-devel
BuildRequires: libX11-devel

%description
pdf417_encode is a program that converts ascii text to the pdf417 barcode standard.
It supports text compression, numeric compression and byte compression.
It currently produces postscript and pbm output for the barcode.

%prep
%setup -q -n pdf417_enc.%{version}
sed -i 's|-lX11|-lX11 -Wl,--allow-multiple-definition|' Makefile

%build
make clean
make
make libpdf417enc.so

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 755 pdf417_enc $RPM_BUILD_ROOT%{_bindir}/pdf417_enc
install -D -m 755 libpdf417enc.so $RPM_BUILD_ROOT%{_libdir}/libpdf417enc.so

%files
%{_bindir}/pdf417_enc
%{_libdir}/libpdf417enc.so

%changelog
* Mon Jan 30 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 4.5
- Rebuilt for Fedora
* Sun Mar 02 2008 Silvan Calarco <silvan.calarco@mambasoft.it> 4.4-1mamba
- update to 4.4
* Thu Jun 09 2005 Alessandro Ramazzina <alessandro.ramazzina@qilinux.it> 4.1-2qilnx
- rebuild and moved from devel-contrib repository to devel repository
* Wed Jun 8 2005 Matteo Bernasconi <voyagernm@virgilio.it> 0.98-1qilnx
- First Build

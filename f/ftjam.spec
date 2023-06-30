%undefine _debugsource_packages

Name:          ftjam
Version:       2.5.2
Release:       4.1
Summary:       A small build tool that can be used as a replacement for Make
Group:         Applications/Development
URL:           https://freetype.fis.uniroma2.it/jam/index.html
Source:        https://switch.dl.sourceforge.net/sourceforge/freetype/ftjam-%{version}.tar.bz2
License:       GPL
BuildRequires: byacc
Provides:      jam

%description
Jam is a small open-source build tool that can be used as a replacement for Make.
Even though Jam is a lot simpler to use than Make, it is far more powerful
and easy to master. It already works on a large variety of platforms
(Unix, Windows, OS/2, VMS, MacOS, BeOS, etc.), it is trivial to port,
and its design is sufficiently clear to allow any average programmer to extend it
with advanced features at will.

This is an improved version, named ‘FT Jam’, containing several enhancements
(like the ability to run on Windows 9x systems, or additional compiler/toolset support).

%prep
%setup -q

%build
%configure
# FIXME: disable strict-aliasing as a workaround against GCC 4.2 of it segfaults
make CFLAGS="-g -O2 -fno-strict-aliasing"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/jam
%doc CHANGES README README.ORG

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5.2
- Rebuilt for Fedora
* Thu Dec 06 2007 Silvan Calarco <silvan.calarco@mambasoft.it> 2.5.2-1mamba
- package created by autospec

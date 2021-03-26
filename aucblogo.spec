%undefine _missing_build_ids_terminate_build

Name:		aucblogo
Version:	4.7
Release:	1.bin
Summary:	Another interpreter for the Logo programming language
Group:		Development/Languages
License:	GPL
Vendor:		Andreas Micheler <Andreas.Micheler@Physik.Uni-Augsburg.de>
Source0:	http://www.physik.uni-augsburg.de/~micheler/aucblogo-4.7-ubuntu-6.06-i386.deb
URL:		http://www.physik.uni-augsburg.de/~micheler
Requires:	ncurses portmidi libtiff expat wxGTK expat-devel
Requires:   avifile
ExclusiveArch: %ix86
AutoReqProv: off

%description
aUCBLogo is a freeware interpreter for the Logo programming language.
It is based on the famous UCBLogo written by Brian Harvey,
Daniel Van Blerkom, Michael Katz and Douglas Orleans.

%prep
%setup -T -c
ar -x %{SOURCE0}

%build

%install
mkdir -p %{buildroot}
tar xf data.tar.gz -C %{buildroot}
mv -f %{buildroot}%{_datadir}/applications/kde/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
ln -s libportmidi.so.0 %{buildroot}%{_libdir}/libporttime.so.0

%files
%{_bindir}/*
%{_libdir}/lib*
%{_libdir}/wx*
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

%changelog
* Mon Jan 20 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 4.7
- Initial binary package

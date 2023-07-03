Name: 		pitchtune
Summary: 	An instrument tuner
Version: 	0.0.4
Release: 	8.1
License:        GPL
Group: 		Applications/Multimedia
Source: 	pitchtune-0.0.4.tar.gz
URL:		https://ip.bourget.cc:8080/pitchtune
Patch0: 	pitchtune-0.0.4-fc4.patch
BuildRequires:  libpng-devel
BuildRequires:  gtk2-devel, alsa-lib-devel

%description
Precise Instrument Tweaking for Crispy Harmony - tuner is a
GPL'ed GTK oscilloscope-style musical instrument tuning program.
It can also be used to find the frequency of sounds.

%prep
%setup -q 
%patch0 -p1 -b .fc4

%build
export LDFLAGS="-Wl,--allow-multiple-definition -lm"
cat TODO > NEWS
./configure --prefix=$RPM_BUILD_ROOT/usr
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr
make install
mv $RPM_BUILD_ROOT/usr/man $RPM_BUILD_ROOT%{_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_datadir}/doc/%{name}-%{version}
%{_datadir}/man/man1/%{name}.1*

%changelog
* Tue May 17 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.4
- Rebuilt for Fedora

* Tue Sep 20 2005 - Chris McBride
- New version 0.0.4
- Patch to change default ALSA device

* Fri Sep 09 2005 - Chris McBride
- Re-Packaged for Fedora Core 4

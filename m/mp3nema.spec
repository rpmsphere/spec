%undefine _debugsource_packages

Name:         mp3nema
Summary:      MP3 Steganography Tool
URL:          https://www.757labs.com/projects/mp3nema/
Group:        Steganography
License:      GPL
Version:      0.4
Release:      6.1
Source0:      https://www.757labs.com/projects/mp3nema/releases/mp3nema-v0_4.tar.gz

%description
MP3nema is a tool aimed at analyzing and capturing data that is
hidden between frames in an MP3 file or stream, otherwise noted as
"out of band" data. This utility also supports adding data between
frames, and capturing streaming audio.

%prep
%setup -q -n mp3nema-v0_4

%build
./configure \
    --prefix=%{_prefix}
%{__make} %{_smp_mflags -O}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p -m 755 \
    $RPM_BUILD_ROOT%{_bindir}
install -c -m 755 \
    mp3nema $RPM_BUILD_ROOT%{_bindir}

%files
%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuilt for Fedora

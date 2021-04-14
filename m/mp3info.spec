Name:         mp3info
Summary:      MP3 Tag Utility
URL:          http://www.ibiblio.org/mp3info/
Group:        Audio
License:      GPL
Version:      0.8.5a
Release:      5.1
Source0:      ftp://ftp.ibiblio.org/pub/linux/apps/sound/mp3-utils/mp3info/mp3info-%{version}.tgz

%description
MP3Info is a little utility used to read and modify the ID3 tags
of MP3 files. MP3Info can also display various techincal aspects of
an MP3 file including playing time, bit-rate, sampling frequency and
other attributes in a pre-defined or user-specifiable output format.

%prep
%setup -q

%build
%{__make} %{_smp_mflags -O} mp3info \
    CC="%{__cc}" \
    CFLAGS="%{optflags -O} %{optflags ncurses .} -Wno-format-security" \
    LIBS="%{optflags} -lncurses"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p -m 755 \
    $RPM_BUILD_ROOT%{_bindir} \
    $RPM_BUILD_ROOT%{_mandir}/man1
install -c -m 755 \
    mp3info $RPM_BUILD_ROOT%{_bindir}
install -c -m 644 \
    mp3info.1 $RPM_BUILD_ROOT%{_mandir}/man1

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.5a
- Rebuilt for Fedora

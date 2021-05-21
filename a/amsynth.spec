%global orig_name amSynth

Name: amsynth
Version: 1.3svn444
Release: 14.1

Summary: Virtual-analog polyphonic synthesizer for ALSA, OSS and JACK
License: GPLv2
Group: Applications/Multimedia
URL: http://code.google.com/p/%{orig_name}

#svn checkout http://amsynth.googlecode.com/svn/trunk amsynth
Source0: %{orig_name}-%{version}.tar.bz2
Source1: %{name}.png
Patch0: %{orig_name}-1.3svn444-desktop-fix.patch

BuildRoot: %{_tmppath}/%{orig_name}-%{version}-%{release}-root
BuildRequires: libpng-devel
BuildRequires: alsa-lib-devel
BuildRequires: gcc-c++
BuildRequires: gtkmm24-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsndfile-devel
#BuildRequires: alsa-oss-devel
BuildRequires: desktop-file-utils

%description
AmSynth is a standalone polyphonic subtractive synthesizer which supports
OSS, ALSA and JACK for Audio and MIDI I/O. Features are as follows.

- Dual oscillators with classic waveforms - sine / saw / square / noise
- 24 dB/oct low-pass resonant filter
- Independent ADSR envelopes for filter & amplitude
- LFO which can module the oscillators, filter, and amplitude
- Distortion effect
- Reverb

For more details see http://code.google.com/p/amsynth/

%package doc
Summary: Documentation for %{name}
Group: Documentation
BuildArch: noarch

%description doc
AmSynth is a standalone polyphonic subtractive synthesizer which supports
OSS, ALSA and JACK for Audio and MIDI I/O.

This package contains the documentation for %{name}

%prep
%setup -q -n %{orig_name}-%{version}
%patch0 -p1
sed -i '1i #include <unistd.h>' src/Config.cc

%build
./autogen.sh
%configure
%__make %{?_smp_mflags}

%install
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT

# Desktop file
%__install -dm 755 $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
   --delete-original \
   --vendor "" \
   --dir $RPM_BUILD_ROOT%{_datadir}/applications \
   $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

# Icon has an odd size, new icon in freedesktop location
rm $RPM_BUILD_ROOT%{_datadir}/pixmaps/amsynth.png
%__install -dm 755 $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/
%__cp -Pp %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/

%clean
%__rm -rf $RPM_BUILD_ROOT

%post
touch --no-create %{_datadir}/icons/hicolor/48x48/apps &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor/48x48/apps &> /dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor/48x48/apps &> /dev/null || :
fi

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor/48x48/apps &> /dev/null || :

%files
%defattr(-,root,root)
%{_bindir}/%{orig_name}
%{_datadir}/%{orig_name}
%{_datadir}/icons/hicolor/48x48/apps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%files doc
%defattr(-,root,root)
# ChangeLog and NEWS are empty
%doc AUTHORS COPYING README SKINNING

%changelog
* Mon Feb 13 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3svn444
- Rebuilt for Fedora

* Tue Nov 01 2011 Simon Lewis <simon.lewis@slnet-online.de> - 1.3-svn444.0.sl
+ Beta 2 too buggy - use svn instead
* Tue Nov 01 2011 Simon Lewis <simon.lewis@slnet-online.de> - 1.3-beta2.0.sl
+ Initial build

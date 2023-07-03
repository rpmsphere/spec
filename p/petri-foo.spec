%undefine _debugsource_packages

Name: petri-foo
Version: 0.1.87
Release: 9.1
Summary: Specimen Sampler project
License: GPLv2
Group: Applications/Multimedia
URL: https://petri-foo.sourceforge.net/
Source0: https://sourceforge.net/projects/petri-foo/files/Source/%{name}-%{version}.tar.bz2
BuildRequires: libpng-devel
BuildRequires: alsa-lib-devel
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: glib2-devel
BuildRequires: gtk2-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libgnomecanvas-devel
BuildRequires: libsamplerate-devel
BuildRequires: libsndfile-devel
BuildRequires: libxml2-devel
BuildRequires: perl
BuildRequires: pkgconfig
BuildRequires: desktop-file-utils
BuildRequires: openssl-devel
BuildRequires: w3m

%description
Petri-Foo is a fork of the Specimen Sampler project. Specimen was 
originally developed by Pete Bessman. See the AUTHORS file for
the list of other authors who've made contributions.

Petri-Foo is forked and developed by James Morris (Feb 2011 +),
with recent code contributions by Brendan Jones (July 2011 +).

Differences, additions and improvements over Specimen
------------------------------------------------------
  * Default patch with saw-wave sample.
  * Raw/Headerless sample file loading.
  * JACK session support.
  * Auto-Preview samples within the file selector.
  * User-interface updated to contemporary GTK2 standards.
  * Improved waveform rendering.
  * Improved visual indication of play and loop selections.
  * Play and loop point navigation.
  * Improved waveform zooming, and addition of mouse-wheel zooming.
  * Fading and X-Fading of sample.
  * Improved MIDI CC handling.
  * User-configurable modulation routing of ADSR, LFO, and MIDI CC.
  * Keyboard tracking, and inverted keyboard tracking.
  * Overall ADSR time scalable by keyboard tracking.
  * Per-patch velocity range.
  * Invertible velocity sensing.
  * Amplitude modulation of LFO output.
  * Removal of deprecated code, and customized PHAT library
    for an improved life-span.
  * Last-used directory recall.
  * Shift/Control + Left-Mouse-Click for increased slider precision.
  * JACK Audio output only, ALSA audio output removed[2].
  * Removed LASH support.

%prep
%setup -q

# Convert to utf-8 and remove dos line endings
for file in AUTHORS BUGS ChangeLog COPYING NEWS PETRI-FOO_ORIGINAL_FILES README TODO TODO.specimen WISHLIST; do
   sed "s|\r||g" $file > $file.new && \
   iconv -f ISO-8859-1 -t UTF-8 -o $file.newer $file.new && \
   rm -f $file.new && \
   touch -r $file $file.newer && \
   mv -f $file.newer $file
done

# Reduce catagories to the minimum valid for all distros
%__perl -p -i -e "s|Audio;AudioVideo;AudioVideoEditing;X-Jack;Midi;X-Alsa;|AudioVideo;Midi;|g" %{name}.desktop

%build
export LDFLAGS=-Wl,--allow-multiple-definition
cmake . \
   -DCMAKE_INSTALL_PREFIX:STRING=%{_prefix} \
   -DUpdateMime=0 \
   -DBuildForDebug=0 \
   -DBUILD_SHARED_LIBS:BOOL=OFF

%__make %{?_smp_mflags} BuildForDebug=0

%install
%__rm -fr $RPM_BUILD_ROOT
%__make DESTDIR=$RPM_BUILD_ROOT install

# Desktop file
%__install -dm 755 $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
   --delete-original \
   --vendor "" \
   --add-category="AudioVideo;Midi;" \
   --dir $RPM_BUILD_ROOT%{_datadir}/applications \
   $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%clean
%__rm -fr $RPM_BUILD_ROOT

%post
update-mime-database %{_datadir}/mime &> /dev/null
touch --no-create %{_datadir}/pixmaps &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/pixmaps &> /dev/null
    gtk-update-icon-cache %{_datadir}/pixmaps &> /dev/null
fi
update-mime-database %{_datadir}/mime &> /dev/null || :

%posttrans
gtk-update-icon-cache %{_datadir}/pixmaps &> /dev/null || :

%files
%doc AUTHORS BUGS ChangeLog COPYING NEWS PETRI-FOO_ORIGINAL_FILES README TODO TODO.specimen WISHLIST
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/pixmaps
%{_datadir}/%{name}/pixmaps/%{name}.png
%{_datadir}/%{name}/pixmaps/%{name}_small.png
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Jan 07 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.87
- Rebuilt for Fedora
* Thu Dec 15 2011 Simon Lewis <simon.lewis@slnet-online.de> - git20111211-1.sl
+ Various changes to make openBUILD happy!
* Mon Dec 12 2011 Simon Lewis <simon.lewis@slnet-online.de> - git20111211-0.sl
+ Initial build

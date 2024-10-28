Name:          timemachine
Version:       0.3.3
Release:       9.1
Summary:       Records audio up to ten seconds ago
Group:         Graphical Desktop/Applications/Multimedia
URL:           https://plugin.org.uk/timemachine/
Source:        https://plugin.org.uk/timemachine/timemachine-%{version}.tar.gz
License:       GPL
BuildRequires: libpng-devel
BuildRequires: alsa-lib-devel
BuildRequires: atk-devel
BuildRequires: cairo-devel
BuildRequires: gtk2-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: lash-devel
BuildRequires: ncurses-devel
BuildRequires: pango-devel
BuildRequires: readline-devel
BuildRequires: libsndfile-devel

%description
I used to always keep a minidisc recorder in my studio running in a mode where
when you pressed record it wrote the last 10 seconds of audio to the disk and
then caught up to realtime and kept recording. The recorder died and haven't
been able to replace it, so this is a simple jack app to do the same job.
It has the advantage that it never clips and can be wired to any part of the
jack graph.

The idea is that I doodle away with whatever is kicking around in my studio
and when I heard an interesting noise, I'd press record and capture it,
without having to try and recreate it. :)

I've been using it to record occasional bursts of interesting noise from jack
apps feeding back into each other. It seems to be stable for me, but there
could be threading issues and race condidtions if run without SCHED_FIFO
(ie. without jackd -R).

%prep
%setup -q

%build
export LDFLAGS=-lm
%configure --prefix=%{_prefix}
make
chmod 755 src/%{name}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/pixmaps
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/applications

%{__install} -m 644 pixmaps/%{name}-icon.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Timemachine
Comment=Jack Time Machine
Exec=timemachine
Icon=timemachine
Terminal=0
Type=Application
Categories=Application;AudioVideo;
EOF

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}
%doc COPYING ChangeLog

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.3
- Rebuilt for Fedora

* Wed Sep 23 2009 Automatic Build System <autodist@mambasoft.it> 0.3.3-1mamba
- automatic update by autodist

* Fri Jul 10 2009 Automatic Build System <autodist@mambasoft.it> 0.3.2-2mamba
- automatic rebuild by autodist

* Wed Mar 25 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 0.3.2-1mamba
- update to 0.3.2

* Wed Aug 27 2008 gil <puntogil@libero.it> 0.3.1-1mamba
- added desktop file

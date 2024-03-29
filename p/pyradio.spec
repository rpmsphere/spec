Name:           pyradio
Version:        0.8.9.28
Release:        1
Summary:        Curses based internet radio player
License:        MIT
URL:            https://www.coderholic.com/pyradio
Source0:        https://github.com/coderholic/pyradio/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
#BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
## MANUAL BEGIN
Recommends:     vlc-noX
## MANUAL END
BuildArch:      noarch

%description
A command line Internet radio player based on curses, that uses external media
players to perform the actual playback. It currently supports the following
players: MPV, MPlayer and VLC.

%prep
%autosetup
mv LICENCE LICENSE

%build
export LC_ALL=en_US.utf8
%py3_build

%install
%py3_install
install -Dm0644 pyradio.1 %{buildroot}%{_mandir}/man1/pyradio.1
#%python_expand %fdupes %{buildroot}%{python3_sitelib}/

%files
%doc Changelog radio-browser.md README.md
%license LICENSE
%{_bindir}/pyradio
%{_mandir}/man1/pyradio.1*
%{python3_sitelib}/*

%changelog
* Sun Nov 20 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.9.28
- Rebuilt for Fedora
* Mon Sep  6 2021 malcolmlewis@opensuse.org
- Updated to version 0.8.9.9:
  * Search history navigation will work with normal keys in
    addition to Control-key combinations (when a line editor does
    not have the focus).
  * When navigating to a new search term, in the RadioBrowser
    Search Window, the two main check boxes will always get the
    focus (makes it easier to navigate using normal keys).
  * Docs Updated
- Changes from version 0.8.9.8:
  * Fixing RadioBrowser history save confirmation window.
  * Interchanging ^T and ^Y in the RadioBrowser Search Window.
  * Addinf FULL_SCREEN_MODES for farter rendering.
- Changes from version -.8.9.7:
  * All Search Window movement keys (^N, ^P, ^Y) ill add a new
    history item (if possible).
  * ^B does not save history to file.
  * Do not close browser if network fails.
- Changes from version 0.8.9.7:
  * RadioBrowser History Management finalized.
  * Fields' placement fixed in RadioBrowser Search Window.
  * RadioBrowser readme page added.
  * Docs updated.
- Changes from 0.8.9.2:
  * Screen flickering when moving within the stations' list
    eliminated.
  * VLC player is available again (disabled by unreported bug).
  * Advancing Radio Browser support.
  * Fixing python 2 return from Radio Browser TUI breakage.
  * Adding dnspython module availability check.
- Changes from version 0.8.9.1:
  * Implemented the so called "Listening" mode, in which PyRadio
    TUI can be reduced down to a single line (the "Status Bar").
    Requested for tilling WM use, (gh#coderholic/pyradio#128).
- Changes from version 0.8.9:
  * Implemented a simplified method to install, update, uninstall.
  * PyRadio will detect its player abnormal termination.
  * Player's connection timeout can now be disabled. Once a player
    is started, it will be considered to be connected immediately.
  * stations.csv changes can now be integrated into user's
    stations.csv.
  * mplayer "pyradio" profile will use the internal mixer to adjust
    volume.
  * BUG FIX: Active players parameter list is always synchronized
    to saved.
  * BUG FIX: Clicking on empty space (past last station) will not
    crash pyradio.
- Changes from version 0.8.8.5:
  * Fixing -ap value not activated by player.
  * Commenting out excessive error log messages.
- Changes from version 0.8.8.4:
  * Fixing double click behavior (while in playback double clicking
    to a different station will start it.
  * vcl will not start muted (volume = 0)
- Changes from version 0.8.8.3:
  * Basic mouse support implemented.
  * Config option to enable mouse support added.
  * Implementing players extra parameters set.
  * Player selection Config window redesigned.
  * Adding -ep. -ap, -lp command line parameters.
  * Fixing a bug which would lead to a crash when "r" would be
    pressed in the config window.
  * Playback will be restarted when vital parameters are changes
    (encoding, connection type, player parameters).
  * When restarting playback, play the correct station not the
    selected one.
  * Adding autostart BAT file on Windows to prevent session locking
    when Windows terminate while PyRadio is still running.
  * pyradio will always use a profile
  * Fixing several minor bugs.
- Changes from version 0.8.8.2:
  * Gracefully exit when the terminal is closed.
- Changes from version 0.8.8.1:
  * Restarting radio-browser.info implementation.
- Changes from version 0.8.8:
  * Implementing "Paste to playlist" (\p) command.
  * Implementing "Create Playlist" (\n).
  * Addind \u (show Unnamed Register) command.
  * Fixing volume display for MPV on python3 before a valid Title
    has been received.
  * Revert to stations playlist if default one (set by config) does
    not exist.
  * Second level config windows will not be displayed when main
    window shows "Window too small" message.
  * When opening a playlist/register from register mode, continue
    playing active station (if found in opened playlist/register).
  * Do not show "'" when opening a playlist/register from register
    mode.
  * "Title: (null)" will not appear any more (vlc).
* Sun Mar  1 2020 malcolmlewis@opensuse.org
- Update to version 0.8.7.1:
  * Fixing mpv playlist option (for mpv 0.32.0).
* Wed Jan  8 2020 Tomáš Chvátal <tchvatal@suse.com>
- Fix the download url.
* Thu Jan  2 2020 malcolmlewis@opensuse.org
- Updated to version 0.8.7:
  * Fixing volume issue with mpv 0.30.0.
  * mpv on python3 uses socket only (no stdout parsing).
  * socat is no longer needed to use mpv.
  * Player's config file will be saved even if it does not already
    exist.
- Changes from version 0.8.6:
  * Adding playlist history (for local playlists).
  * https URLs will be converted to http before connecting.
  * Fixing station moving when appending station.
  * Config / Default station: pading fixed.
- Changes from version 0.8.5:
  * PyRadio will not crush with mpv 0.30.0, changing mpv's volume
    is still possible, but no info will be presented on the Status
    Bar. Furthermore, saving mpv's volume will not be possible,
    (gh#mpv-player/mpv#7153).
  * When the default played is changed in the config, a message
    to restart the application is presented to the user.
  * Config / Default station: pading fixed.
* Fri Nov 15 2019 malcolmlewis@opensuse.org
- Initial build at version 0.8.4.

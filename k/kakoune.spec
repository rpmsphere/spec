Name:           kakoune
Version:        2019.07.01
Release:        1
Summary:        A code editor heavily inspired by Vim
License:        Unlicense
Group:          Productivity/Text/Editors
URL:            http://kakoune.org/
Source:         %{name}-%{version}.tar.gz
BuildRequires:  asciidoc
BuildRequires:  libxslt
BuildRequires:  ncurses-devel
BuildRequires:  boost-devel

%description
Kakoune is a code editor heavily inspired by Vim.
It's faster as in less keystrokes, supports multiple selections and uses orthogonal design.

%prep
%setup -q -n %{name}-%{version}/src

%build
%make_build
#make %{?_smp_mflags} CXXFLAGS="%{optflags} -std=gnu++14"

%install
make %{?_smp_mflags} install PREFIX=%{buildroot}%{_prefix}
rm -rf %{buildroot}%{_datadir}/doc

%files
%doc ../UNLICENSE
%{_bindir}/kak
%{_datadir}/kak
%{_mandir}/man1/kak.1*

%changelog
* Wed Sep 11 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2019.07.01
- Rebuilt for Fedora
* Tue Feb 27 2018 mliska@suse.cz
- Update to version kakoune-0.0+git.20180228.
- Bump ncurses requirement to version 6.0 and higher.
* Thu Oct 19 2017 mpluskal@suse.com
- Update to version 0.0+git.20171017:
  * Tweak buffer change code so that WinDisplay hooks can use info boxes
  * Add a basic replace-ranges highlighter
  * doc: Document the -E flag
  * kakrc: Simplify and optimize the autoload function
  * Fix reference to kakrc highlighter for markdown
  * Improve kakrc highlighter with more static words
  * Remove ad-hoc rules in kakrc highlighter
  * Add some missing languages to comment.kak
  * Highlight object keys in yaml
  * rc: Document non-hidden options with `-docstring`
  * rc: Use POSIX `command -v` instead of `which`
  * rc: Simplify and optimize the `alt` command
  * Document that markup is possible in completion menu entries.
  * Document escape key and update Q doc according to normal.cc
  * Rename range-faces to range-specs
  * Add range-faces -> range-specs rename to the breaking changes message
  * Add missing std::move in on_scope_end implementation
  * small code cleanups
  * Highlight 'copied' file action in git-commit buffers
  * Move constexpr compatible Array struct to meta.hh
  * Small reorganization in the normal keymap
  * Make hardware cursor visible in ncurses ui
  * Add modified value if buffer has modifications not saved
  * Change <a-z>/<a-Z> to combine selections instead of appending
  * Support aligning to opening { as well as ( in c-family indent
  * Changed wording of completers description
  * do not embed timestamps in .gz files
  * Always link input files in the same order
  * Commit correct version of c-family indent change
  * Fix vertical movement with tabstops
  * Smarter align to opening parenthesis/brace supporting multiline
  * Add some missing tests for c-family indent
  * Fix scrolling when cursor is on a wrapped part of the last displayed line
  * Remove virtual destructor from OptionManagerWatcher
  * Fix bug where idle timers of disabled modes were still run
  * Do not avoid eol in insert mode vertical movement
  * Fix man.kak when man pages filenames just end up with the manual section
  * Remove unneeded forward declaration
  * Fix hardware cursor positioning in prompt when status bar is on bottom
  * Small code tweak
  * Rename line-flags option type to line-specs
  * Add support for raw C++ strings in c-family highlighting
  * Fix command parsing bug when commenting after a command
  * Add an update-option command to update range-descs/line-descs options
  * Document the update-option command
  * Add break and continue to the list of sh keywords
  * Use a line-specs for the clang_errors option in clang.kak
  * Make the lint_errors a range-specs option in lint.kak
  * Make shell variable expansion in "strings" highlighted the same way as in code
  * Expose last entered command in register :
  * Modernize the way we compute memory domains from type
  * Small documentation tweak in display_buffer.hh
  * Small code style tweak
  * Use a ScopedSetBool instead of manual set/unset for InputModes::Normal::m_in_on_key
  * Small formatting tweak
  * Remove unused and potentially error prone constructor from ArrayView
  * Remove unneeded explicit conversion
  * doc: Update the F.A.Q.
  * Slight style tweak in doc.kak
  * Small code tweak
  * Document line-flags -> line-specs and update-option in breaking changes
  * Parse meta as 8 bit in Normal mode to fix the terminals using that
  * Highlight non numeric man sections as well in man.kak
  * Put the doc/manpages/ pages in the 'k' section
  * man.kak: Rename _manpage option to manpage
  * Use more precise wording for object selection info box
  * Fix typos in info-box: availabe, encodngs, highglighters…
  * Exclude debug from eval/exec over all buffers
  * Change ncurses_ui info box generation logic to use a Vector<String>
  * Tweak alias command docstring not to end up with an eol
  * Re-hide hardware cursor, seems its causing troubles with various terminal emulator
  * fix: remove duplicate include to containers.hh in face_registry.cc
  * docs: add missing angle brackets around keys in README and manpages
  * Refine info titles to distinguish G and V modes
  * Add SVG detection as xml in file.kak
  * Add support for more selection combining operations
  * Small formatting fix
  * Rename _grep_current_line option to grep_current_line
  * Support option_add for HashMap options
  * Strip surrounding whitespaces in `*`
  * Document the `*` behaviour change in the startup message
  * doc: Fix the documentation of the `alt_dirs` option
  * Change RankedMatch ordering to favor `/` characters
  * Improve readability of command docstrings by changing formatting
  * Log errors written to the status line inside the debug buffer as well
  * Revert "doc: Fix the documentation of the `alt_dirs` option"
  * Fix spurious copies being made when using the format function
  * Remember previous NormalParams::count in view-lock mode
  * Add underscore char as a valid punctuation for text-object pairs
  * Expose kak_buf_line_count
  * Clarify rotation direction between <'> and <a-'> in info help
  * Use a vector instead of a hash map to store hooks
  * Use String default ctor instead of empty string
  * Fix useles copy of hook_func in HookManager::add_hook parameter
  * noexept-ify BufferIterator methods
  * noexcept-ify utf8::iterator methods
  * Small style tweak
  * Move NestedBool to utils.hh
  * Avoid expensive copies of Hooks in HookManager::run_hooks
  * Move hook executing logic into HookManager
  * Fix missing hook removal command in c-family.kak
  * Do not allow whitespaces as %% string delimiters
  * Use range based accumulate wrapper instead of std::accumulate
  * Remove unneeded unknown_expand exception type
  * Fix memory errors due to sharing the MatchResults in the Hooks struct
  * Change merge_overlapping to guarantee we dont break the sorting
  * Use range based find_if wrapper for finding shell env vars
  * Run BufCreate hook *before* Buf{Open,New}File
  * Use microseconds instead of milliseconds for built-in profiling
  * Only trigger PromptEvent::Change on idle
  * Do not disable incsearch option in context wrap
  * Filter debug buffers before creating the SafePtr vector in -buffer *
  * Move variable closer to its point of use
  * Add `-width <max_width>` support in the wrap highlighter
  * Disable idle timers on all transient contexts
  * Fix quadratic behaviour in when selecting an insert completion
  * Do not show startup info when piping into kak
  * Remove spurious double underscore
  * Add Alacritty
  * More explicit and simpler code
  * Rename 'unit' test directory to 'normal' as they are the normal mode tests
  * Add horizontal/vertical scrolling display tests
  * Add some unit tests for horizontal scrolling with tabulations
  * rc: Fix calls to `mktemp`
  * rc jedi: Don't create an unused debug/log file
  * Rework partial line display logic
  * Proper linear time insert completion insertion
  * Fix bug in word completer
  * Simplify column highlighter and make it more robust
  * Remove unused only_buffer mode for DisplayLine::trim
  * Fix wrapping support
  * gitignore backup files
  * Remove backup file from git
  * Fix the Buffer::end() madness
  * Fix corner case in compute_modified_ranges
  * Use read_fd to get pipe command from stdin instead of ad-hoc code
  * Simplify a bit buffer iteration functions
  * minor style tweak
  * Always store InclusiveBufferRange with first < second
  * Fix corner case in C family indenting
  * Change custom text object desc trigger from ':' to 'c' - Fix #1362
  * Update Homebrew install tip in README
  * Respect scroll offset even when wrapping lines
  * Use more correct `[ -f <file> ]` in test runner
  * doc: Unify the documentation for menu keys
  * rc ctags: Make commands follow the naming convention
  * Change window display to not use invalid buffer coordinates
  * Go back to window lines ending at one past the end of the buffer line
  * Fix crash recently introduced when deleting at buffer start in insert mode
  * Move tolerance for one past end of line coordinates to highlighter code
  * Fix some other uses of invalid buffer coordinates in display code
  * Fix some remaining uses of invalid atom coordinates
  * rc: Fix calls to `mktemp`
  * Hide info/menu when they are anchored to an invisible buffer coord
  * Support hitting escape to cancel a selection combine operation
  * Add fallthrough comment to silence gcc-7 warning
  * Fix asciidoc formatting in README
  * Trim whitespaces surrounding docstrings
  * Update command names
  * Disable -Wnoexcept-type warning
  * Update startup info message
  * src: Add a `commands` debug flag
  * src: Add `profile-hash-maps` to the `debug` command's docstring
  * Correctly handle tabs when show_whitespaces is added
  * Use already stored coordinates in show_whitespaces
  * Use user-supplied autoshowcompl option's value.
  * rust highlighter: '"' is not the start of a string
  * apply '"' highlighting fix to haskell as well
  * doc: Mention the proper environment variable for pagers
  * doc: Explain why `a` modifies the selection and `i` doesn't
  * Use an HashMap to store options in option manager
  * Do not set idle timers when running in a transient context
  * Add ctags command renaming info in the startup message
  * rc formatter: Make sure the formatter returned successfully
  * Slight code refactoring and perf improvement in vector option to string
  * Remember count when repeating last insert
  * Fix various undefined behaviours detected by UBSan
  * Disable -Wunknown-attributes
  * Formatting fix
  * Always use the base LineNumber face for the line number separator
  * Change completion_extra_word_char to be a list of codepoints instead of a string
  * Remove useless Vector, use a ConstArrayView instead
  * Pass a context instead of just the buffer to selector functions
  * Use the extra_word_chars option in word based normal commands
  * Fix replacing last eol with a single eol
  * Fix reference highlighter not forwarding compute_display_setup
  * Docs: add more details about hooks
  * Add error message when using format command with no formatcmd specified
  * Ensure cursor stays visible with wrapped line bigger than window
  * Do not allow repeating last insert when we are not in normal mode
  * Consider non-files buffers as never modified
  * Validating an empty command in prompt reruns the last command
  * Code style tweak
  * Remove some dead code
  * Formatting tweak
  * contrib Tupfile: Adapt to upstream changes
  * rc tupfile: Fix the keywords regex
  * rc c-family: Add a hook to the insert group
  * Docs: add missing PromptIdle hook mentions
  * Refine info titles to distinguish f/t (select) and F/T (extend)
  * Make register and completion autoinfo lists uniform with all the other ones
  * Treat non printable characters as zero-width instead of -1 width
  * Formatting fixes
  * Fix trailing whitespaces in README
  * Highliight git MERGE_MSG files as commit messages
  * Remove assert in String::String(Codepoint, ColumnCount)
  * Docs: add missing <a-R> key and fix info message
  * Docs: add missing colon register (last entered command)
  * Add <a-o> and <a-O> to add lines below/above selections
  * Preserve order of definition of mappings when listing them
  * Add <a-c> and <a-d> for changing/deleting without yanking
  * Alternative, and hopefully safer implementation of <a-o>/<a-O>
  * Small startup message formatting tweak
  * Add main selection index in mode_info
  * Docs: update completions_extra_word_chars → extra_word_chars
  * Fix undo handling in <a-o>/<a-O>
  * Fix an assert in compute modified ranges when merging single char ranges
  * Fix assertion when replacing with empty strings
  * `|` now applies the diff of the modification instead of plain replace
  * Fix replacing reducing selections to their cursor
  * rc formatter: Don't force selection restoration
  * Small code cleanup in diff implementation
  * Tolerate that the cursor might not be visible
  * rc git: Don't force a highlighting format on commits
  * Fix xmessage handling in assert.cc
  * Remove MirroredArray for diff implementation
  * Refactor find_diff_rec and detect kept prefix/suffixes early
  * Slight style change
  * rc man: Avoid undefined behavior on `expr`
  * Change diff Implementation to use end indices instead of length
  * More refactoring of the diff code in order to make it cleaner
  * Use the provided equal functor for prefix/suffix detection in diff
  * Add an assert to try to get more info on #1506
  * Migrate code to c++14
  * Fix travis configuration for C++14 support
  * Cleanup some code with C++14 features
  * Use c++14 function deduction and decltype(auto) to cleanup some code
  * Try to simplify back travis config
  * Remove unused function
  * More uses of standard type traits aliases
  * More use of std::enable_if_t alias
  * Update README for C++14 requirement
  * Remove `echo -color` support, superseeded by `echo -markup`
  * Fix main selection handling in keep pipe ($)
  * Detect overflow using a long long for the computation result.
  * Require clang >= 3.6 as 3.5 is failing on debug symbol generation
  * Use smart case matching for contiguous/prefix/fullmatch detection
  * Make non smart case full match better than smart case full match
  * Fix wrong autoinfo for remove-highlighter
  * More cleanups in diff code
  * Limit diff algorithm complexity
  * Do not reject switch parameters starting with `-`
  * Fix sakura termcmd setup
  * Support values starting with `-` for in set-register command
  * Use single_param for ParameterDesc when relevant in command descs
  * Fix grep-jump on eol
  * Fix grep-next/prev-match not jumping correctly to first/last match
  * Check final cursor position in indent/c-family/indent-if-body test
  * Slight formatting tweak
  * More tests for markdown autoindent.
  * Consecutive markdown list bullets are not a valid list prefix.
  * Change documentation directory towards $kak_runtime/doc
  * Fix SafeCountable and RefCountable copy/move logic
  * Purge history on buffer reload when NoUndo flag is on
  * Remove redundant types inside Kakoune::Allocator
  * Remove size redundancy in enum_desc function declaration
  * Use decltype(auto) return type for some to_string functions
  * Style tweak for regex code
  * Change HashCompatible trait to a variable template
  * Do not consider the 8th bit to mean Alt on keys that are mouse events
  * Add missing '&' to last example
  * Try to get make_array to compile with older compiler version
  * Respecify EnumDescs array sizes manually to workaround clang-3.6 bug
  * Revert "Change HashCompatible trait to a variable template"
  * Change selection extension code to be simpler
  * Remove now trivial Selection::merge_with method
  * Show error when using go-jump and jq is not installed
  * Add build type (debug/release) in ":debug info" output
  * Improve Haskell highlighter
  * Update startup info
  * Optimize DisplayBuffer::optimize()
  * Support specifying an exit status on `quit` commands
  * Fix String::Data copying/moving from self
  * editorconfig.kak: fix awk typo
  * doc faq: Document the expansion of shell scopes
  * rc base html: Highlight the DOCTYPE and tag attributes
  * Fix wording in docs for goto commands (h,l,i)
  * doc: Add missing flags to the `debug` option
  * Expose client pid as $kak_client_pid
  * Fix kakmap.rb script for new normal.cc code
  * Adding Ubuntu Tip
  * Fix naming in fd_writable
  * Do not expand env vars in parse_filename
  * Do less implicit parse_filename calls
  * avoid literal eol in status lines, replace them with another symbol
  * Fix shell expand example in README
  * Rework containers.hh to get rid of the Factory structures
  * Rename containers.hh to ranges.hh (and Container to Range)
  * rc base html: Highlight attributes with no value
  * Check for gocode, goimports and gogetdoc on go-tools loading
  * doc: Document the `column` and `line` highlighters
  * Code style tweak in optional.hh
  * Remove unneeded ParameterDesc constructor
  * Make InsertCompletion an aggregate
  * Make Token a simple aggregate
  * Make LineAndColumn an aggregate as well
  * Make Buffer::Modification an aggregate
  * Slight tweak of FaceRegistry::FaceOrAlias definition
  * Add current history id to env variables
  * Add documentation for curr_history_id
  * Rename env variable kak_curr_history_id to kak_history_id
  * css.kak: add hl to more common CSS length units
  * Tolerate unwritable socket when trying to send the disconnection message
  * Small code simplifications
  * Fix typo: to many → too many
  * rc: Add support for Mercurial
  * rc: Add support for MySQL, SQL Server and MS Access
  * Fork server to background when the client/server process receives SIGHUP
  * Add debug faces
  * docs: add command aliases Fix #1556
  * doc faq: Document how to fix the "insert mode escape lag"
  * Rename some string conversion function to the common 'to_string'
  * Hide info box and eventual status message after handling a mouse event
  * Replace invalid codepoints with � instead of U+XXXX
  * Expose the character under the cursor as $kak_cursor_char_value
  * docs: add options default values Fix: #1557
  * rc perl: Don't highlight regex, fix string escapes
  * Fix typo: parmeter → parameter
  * Add count support for scroll keys (PageUp, PageDown, C-bfud)
  * c-family: auto close unions with a semicolon as well
  * Avoid wrapping between punctuation and word
  * Document custom text object move in breaking changes
  * Fix compilation
  * Document what keys are mappable.
  * Add '[debug]' context_info for debug buffers
  * Add max_history_id in status printed with <a-u> and <a-U>
  * Fix missing spaces / new lines in commands docstring
  * Use <esc> to exit on-key modes
  * Add count support for indent / deindent
  * Small code style tweak
  * Fix Lua comment delimiter insertion (see #1584)
  * Add selections_desc format to select autoinfo
  * Fix: glob for backup files.
  * Removing the local client due to SIGHUP is not graceful
  * Add status info when navigating through jumplist (<c-o>, <c-i>)
  * Convert status info into proper runtime_errors
  * Display selections count in insert mode the same it's displayed in normal mode
  * Fix regression test #1435 after a change in the insert modeline format
  * Distinguish between modes being disabled temporarily and definitely
  * Docs: add missing -command-completion and -shell-candidates switches
  * rc doc: Remove window hooks automatically assigned
  * rc doc: Implement the `-i` flag of `sed` in a POSIX manner
  * rc doc: Use POSIX flag `-name` instead of `-iname`
  * rc man/doc: Don't show `groff` warnings
  * Add 'line' in completers option as a way to force explicit <c-x>f
  * Docs: add missing -collapse-jumps and fix -itersel
  * Add debug mappings
  * Docs: add missing normal keys <c-[bfud]>
  * Add client_list var
  * formatting tweak
  * Add more constexpr to flags wrapping functions
  * Allow itersel with draft context to change the buffer
  * Remove unneeded regex.hh include in color.cc
  * Add missing operator+= and -= on utf8_iterator
  * Move HookManager::Hook definition in the cpp
  * Docs: add missing vm and update custom text-object : → c
  * Add is_upper and is_lower helper unicode functions
  * Make utf8_iterator traits clear about it returning non-references
  * Make Server outlive buffer manager
  * Move all non-core string code to string_utils.{hh,cc}
  * Remove unused forward declaration
  * Fix potential bug in clang.kak
  * Fix utf8::to_previous that could go before the begin iterator
  * Add support for typescript
  * Docs: fix wrong hardcoded 100ms value for autocompletion
  * Removed terminal colors from Solarized and added a light variant.
  * Refactor column highlighter to make it more robust
  * Do not restore old backup files. This check is necessary for cases where - the file was edited with a different editor/program or - kak didn't restore a backup or - if old backups weren't purged or - if autorestore wasn't loaded (e.g. `kak -n`) after backups were generated.
  * iterm: use 'exec' so pane auto-closes with editor
  * ref vim options.txt
  * Add a `fail` command to explicitely raise an error
  * Optimize CommandManager::execute handling of tokens
- Drop no longer needed reproducible.patch
* Sun Jul 23 2017 bwiedemann@suse.com
- Update reproducible.patch
  to make the package build fully reproducible (boo#1041090)
* Thu May 18 2017 dziolkowski@suse.com
- Update to version 0.0+git.20170513:
  * Add column information
  * New colorscheme: desertex
  * test: Fix UTF8 compliant locale detection
  * rc: Simplify/POSIXify the `autorestore.kak` script
  * rc: POSIXify the `modeline.kak` script
  * Cleanup some tabby mess in the Makefile
  * Compile optimized and debug into different files, make `kak` a symlink
  * Fix clang warnings about uninitialized timestamp field
  * Small naming tweak
  * add rc/ocaml.kak
  * highlight hash access symbols
  * Add `RawKey` to hook completion list
  * rc: Don't print errors when no buffer backup exist
  * add racer completion for rust
  * rc: POSIX and cosmetic fixes in the `spell` script`
  * rc: add a `spell-next` command
  * src: Fix the string conversion of range faces
  * <space>, <a-space>: throw on invalid preconditions
  * Add docstring support for mappings, and use them in autoinfo
  * Make <a-space> throw on invalid index or last selection
  * Ensure main selection index is correct directly in SelectionList::remove
  * Return an optional selection in most selectors, fail rather than keep current
  * Fix indent selection respect for original selection cursor position
  * Fix tests for indent selection
  * Move object unit tests in their own subfolder
  * Refactor regex based selection code
  * Git ignore kak.opt and kak.debug
  * Refactor surround unit test code
  * Change word object selector to fail if the cursor is not on a word char
  * Remove unused AliasRegistry::flatten_aliases method
  * Add Symbol, async and await highlighting for javascript.kak
  * Document the -docstring switch of the :map command
  * Simplify AliasRegistry::remove_alias
  * escape pipe from closure in the description
  * Introduce a custom HashMap implementation along with a quick benchmark
  * Add support for HashMap options types
  * Replace uses of UnorderedMap with HashMap
  * Replace IdMap with HashMap
  * Remove temporary stats code from HashMap
  * also handle enums explicitly
  * Update Makefile
  * Expand a bit the hash map profiling code
  * Cleanup hash_map code
  * test: Remove empty test directories
  * Small code simplification
  * Collapse undo groups during an eval command
  * Try to please clang-3.5
  * doc: Add an IRC badge linking to Freenode
  * ncurses: Add a Dilbert assistant
  * Add a -debug flag to :edit to set the buffer as debug data
  * Fix crash on non utf8 files trigering highlighting of backward ranges
  * Add dilbert in the ui_options doctring
  * Change lint.kak column display to put it at the end
  * Increase modelinefmt configuration power
  * src: Align the assistant in the middle of the popup
  * src: Make the cursor character an opening delimiter
  * Add regression test for #1105
  * The canonical name for the documentation command is :doc, not :help
  * Move SelectionList::set implementation out of the header
  * Migrate to a more value based meta programming model
  * Migrate WithBitOps template specialization to with_bit_ops function
  * Remove unneeded 'valid' helper template
  * Small code tweaks regarding flags handling
  * Move enum/flags option functions to option_types.hh
  * Try to clean up option include a bit
  * Fixes some clang-tidy warning and add a few missing meta.hh include
  * Use a HashMap to store the normal mode keymap
  * Merge faces in show_whitespaces highlighter instead of replacing it
  * Try to fix clang 3.5 compilation
  * src: Introduce a `-i` suffix flag for filter backups
  * Remove some unneeded type declarations in AliasRegistry
  * Added gruvbox colorscheme
  * src: Fix the `distclean` Makefile target
  * spell.kak: preserve spelling language from :spell in :spell-replace
  * contrib: Remove `make_deb.bash`
  * Add an InsertDelete hook
  * Expose hook params regex captures in hook_param_capture_N
  * rc/ranger: use $kak_hook_param_capture_N
  * Change prompt completion to only update when idle
  * Do not disable autoinfo and autoshowcompl in non interactive context
  * ncurses: When hiding the menu, recompute the info position
  * rc: Export $TMPDIR to new `tmux` processes
  * doc: Fix the name of a now unexisting face
  * rc: Forward $TMPDIR to `iterm` subprocesses
  * src: Support the `-help` flag
  * Add support for parsing multiple modifiers in keys
  * Remove some now unneeded uses of const String& params
  * Change multi modifier key syntax to be <c-a-space> instead of <ca-space>
  * Name key '+' as plus and '-' as minus
  * Place hardware terminal cursor at the current main cursor/prompt cursor position
  * Add documentation for the set_cursor ui call in json_ui.asciidoc
  * Fix tests after addition of the set_cursor UI method
  * When not sending data to a subprocess, close its stdin
  * rc: Properly modify `tmux`'s environment with `env`
  * doc: Write a dedicated "mapping" page
  * Do not try to split non range atoms in column highlighter
  * Fix uninitialised value for cursor mode
  * Safer code for parsing commands
  * Assume filename passed to write_buffer_to_file is already parsed
  * src: Implement a `write!` command
  * Change utf8::to_next/to_previous so that they are more symetrical
  * Fix generation of empty erase changes
  * doc: Fix some issues in spelling, grammar and punctuation
  * Set stdin to /dev/null instead of closing it when we dont have data to pipe to child
  * Add noexcept specifiers to unicode and utf8 functions
  * Style tweak in highglighters.cc
  * doc: document the `X` key
  * Support appending selections to empty register
  * rc: Use $SHELL instead of spawning `bash` arbitrarily
  * Add Elixir highlighter
  * doc: Document guidelines about writing kak scripts
  * doc: Remove Debian from the list of distributions
  * Fix use of invalidated iterator in the command map on exception
  * Do not use any display information to determine where the cursor moves
  * Add a wrap highlighter
  * Introduce highlighting phases and display setup computation
  * Respect tabstop in Buffer::offset_coord
  * Make Wrap highlighter only wrap on window width.
  * Make scrolling around work more correctly with wrapping
  * Introduce a LineNumberWrapped face
  * Disable horizontal scrolling when running a WrapHighlighter
  * Detect errors while parsing flag line and handle them
  * Move passes logic to the base Highlighter class
  * Add a `-passes` switch support for the group highlighter
  * Add support for word wrapping with the -word switch to the wrap highlighter
  * Reject 0 wrap column
  * Document the wrap highlighter
  * Ensure window position line is inside buffer
  * Fix assert when wrapping a line that takes more than the full window height
  * Slight highlighting related code cleanup
  * Fix infinite loop with longer than width words in word wrap mode
  * Fix unneeded and wrong splitting of display atom during wrapping
  * Move SimpleHighlighter as an implementation detail
  * Update wrap highlighter docstring
  * Do not push a final spurious command separators when parsing commands
  * Refactor range highlighting into a struct
  * Distinguish between BufferRanges and InclusiveBufferRanges
  * Fix a few spelling errors detected by spell.kak in the README
  * Update group highlighter docstring to document the passes option
  * Rename kakrc::autoload to kakrc::autoload_directory
  * Make ref highlighter work for all highlight passes
  * Add support for the -passes option to the ref highlighter
  * Small spelling error fix
  * Use LineCount instead of int for ncurses assistant margin
  * Disable horizontal scroll offset support when wrapping
  * Use only default faces
  * fix new face documentation
  * update line-flags and flag_lines doc to reflect current status
  * misc whitespace fix in docs
  * Add the -E switch for server initialization commands
* Sun Apr 30 2017 bwiedemann@suse.com
- Add reproducible.patch to call gzip -n to make build a bit more reproducible
* Sat Feb 25 2017 mpluskal@suse.com
- Update to version 0.0+git.20170223:
  * rename commenting.kak to comment.kak
  * tweak :comment-line behaviour to comment selected lines
  * rename :comment-selection to :comment-block
  * rename line and block comments options
  * fix typo
  * remove optional value
  * fix quote convention
  * Add quote to completion characters in haskell
  * Remove hash from StringData
  * Make BufferIterator only a bidirectional iterator
  * Set commenting options for php
  * Add octothorpe to php comment highlighters
  * Remove unused Diff::posA field
  * Remove unused WindowAndSelections timestamp field
  * Make StringView and unit types trivial types
  * Detect too deep command call stack
  * Remove unneeded assignment to null in RefPtr::release
  * Fix option name in haskell.kak
  * Use iswlower instead of islower
  * Fix some uninitialized values
  * Fix infinite loop when comparing RankedMatches containing invalid utf8
  * Fix autorestore script when we have multiple restore files
  * Fix explicit insert completion menu/info not hiding
  * Warning fix in ranked_match.cc
  * Make SharedString::create take a list of StringViews
  * Rework NCurses key parsing to properly handle <a-special key>
  * Support the vim behaviour for +line syntax
  * Add some noexcept to pointer policies
  * Formatting fix
  * Tweak ranked match ordering
  * Improve POSIX sed compatibility in lint.kak
  * Fix on-key command name in README
  * support in-line comments
  * Change `n` behaviour to only select next match for main selection
  * Use <a-'> for backward rotate selection and move rotate content to <a-">
  * Also execute prompt callback when just starting
  * Document whitespace highlighter
  * Fix doc ui options and manpage
  * Adds tomorrow-night theme.
  * Make piping data into shell commands non blocking
  * Highlight c-family include paths as identifiers
  * Store shell-candidates completions in the Completion memory domain
  * Fix some bugs in non blocking pipe writing
  * Allow modifying the characters used when highlighting whitespace
  * Small layout tweak for Buffer::HistoryNode
  * Make gdb ArrayIterator python 3 compatible
  * Add Regex support in gdb pretty printing
  * Add -match-capture support for regions higlighter
  * Add proper heredoc highlighting support to sh.kak
  * Remove unneeded padding in relative line numbers highlighting
  * Fix Buffer::offset_coord that was dropping the target coordinate
  * Fix missing new line char in declare_option_cmd info
  * Add command completer for types to declare-option
  * fix regex highlighting
  * Refactor show_whitespaces a bit
  * Adds faces module and function. Renames identifier face to variable.
  * Make sure no ANSI sequences are in the data returned by `man`
  * Update outdated example in <a-"> keys doc
  * Add support for -on-change and -on-abort to prompt
  * Add elm language support
  * Fix make.kak handling of 'Entering directory' and absolute paths
  * Fix non-returning parse_key lambda
  * Fix RegisterRestorer not handling potential throws on register assign
  * Make numeric registers setable
  * Reorganize code in main.cc
  * Detect when switches are specified more than once
  * Detect when -client, -buffer or -try-client are used at the same time
  * Small naming tweak in HookManager
  * Copy the list of hooks to run before iterating on them and running them
  * pony.kak: Remove redundant BufNew/BufOpen hooks
  * Rename BufNew and BufOpen hooks to BufNewFile and BufOpenFile
  * Document backslash disabling hooks
  * Fix handling of disabled_hooks regex
  * Display an info box on startup with recent breaking changes
  * Fix hook list in commands.cc
  * Correctly handle mutation of the watcher list while iterating on them
  * Fix performance of word completion with many different selections
  * Fix overly strict backward_sorted_until
  * jedi.kak: python 3 compat fix
  * improved haskell comment regex
  * Refactor test run script
  * Try to please clang-3.5
  * Remove out of date TODO file
  * Properly wrap `kak_assert` into a do-while scope
  * Use false instead of 0 in the kak_assert do while
  * Refactor StringData and StringRegistry to remove need for purging
  * Refactor WordDB::add_words to be slightly faster
  * Slight code cleanup in utf8_iterator.hh
  * Fix support for non ascii chars in completion_extra_word_char
  * Refactor get_words to be simpler and faster
  * Tweak some character categorization function implementations
* Sun Feb  5 2017 mpluskal@suse.com
- Update boost dependencies
* Fri Jan 27 2017 mpluskal@suse.com
- Update to version 0.0+git.20170125:
  * Fix misleading wording
  * Fix escaping
  * Document +line[:column]
  * Add `gi` to go to first non-blank character on line
  * Fix crash when clearing a regex prompt with multiple selections
  * Fix shell context capture that was accessing dead parameters
  * Add a `RawKey` hook for raw user input hooking
  * Rename "shortcuts" manpage to "keys"
  * Add a quick section on key syntax in keys.asciidoc
  * More tolerant recognition of underlined titles in asciidoc highlight
  * Only restore cursor position after an append if we still have cursor > anchor
  * Fix fifo reading not handling potential errors from the read call
* Thu Nov  3 2016 mpluskal@suse.com
- Update to version 0.0+git.20161102:
  * Add to_string(long long int) overload to fix OSX compilation
  * Fix typo in write_cmd's desc
  * Use %%~~ for delimiting to avoid issues with braces in the message
  * lint-prev
  * Use same idiom as for lint-next
  * Remove since it gets overwritten by the NormalIdle hook + $kak_cursor_line will always be 1 as that runs in a temporary context for the window
  * Tweak c-family indentation logic
  * Add experimental static linking support to the makefile
  * Propagate NormalParams to user mappings
* Fri Sep 30 2016 dwaas@suse.com
- Update to version 0.0+git.20160928:
  * add ranger.kak
  * Always use quotes with sh/bash
  * disable hooks
  * fixes 'end' insertion
  * Use POSIX case and BRE
  * fixes symbol highlighting
  * highlight :: operator
  * Make idle timeout and filesystem check timeout configurable
  * Tweak zenburn theme, rely less on terminal builtin colors
  * Rewrite PerArgumentCommandCompleter to use compile time dispatching
  * More command completer code cleanup
  * Add an unmap command to remove key mappings
  * Fix select_to_reverse to correctly handle the first character of the buffer
  * Code cleanup in make_completer, use std::decay
  * Tweak Buffer::offset_coord implementation
  * Add InsertCompletionShow/InsertCompletionHide hooks
  * formatter.kak: Use sed rather than ${variable//string/replacement}
  * Add more standard GNU keywords to the makefile completion keywords
  * Add language highlighting to markdown code blocks
  * Allow dashes in target names for syntax highlighting
  * Indent after other keywords
  * Place the Makefile highlighting script alongside the `make` support script
  * Add some standard GNU targets to the Makefile
  * add ranger.kak
  * Tweak RankedMatch logic, prioritize matches that are in a single word
  * OptionDescs are const in OptionRegistry
  * Assert substr from parameter is within the string
  * Pass count to all object selectors
  * Selecting 'around' word when on spaces after word now selects next word
  * Make hook disabling work for all hooks, not only user hooks
  * Validate option names to be in [a-zA-Z0-9_]
  * Fix String::Data::reserve on big endian platforms, and document String::Data
  * Do not automatically enable ranger on directory open errors
* Thu Sep 15 2016 dwaas@suse.com
- Enabled testsuite
- Specified Requires versions in .specfile
* Thu Sep 15 2016 dwaas@suse.com
- Update to version 0.0+git.20160907:
  * Fix the directory from which the file containing a matching tag will be opened
  * Use proper buffering when reading remote messages
  * Rework client quitting and handling of remote errors
  * Fix handling of remote errors in the accepter
  * Tweak c-family indent logic
  * Small code tweak in generate_switches_doc
  * Use shell-candidates for :colorscheme completion
  * Do not let boost regex errors propagate, convert them to Kakoune errors.
  * Support kill session inside init command
  * Highlight diff in git-commit too
* Thu May  5 2016 mpluskal@suse.com
- Update to version 0.0+git.20160505:
  * add face to change whitespace colors
  * Fix splitting selecting the first buffer char when there is a match at buffer begin
  * fix whitespace label
  * Pierre CLEMENT (pierroelmito) Copyright Waiver
  * Expose a WinResize hook when a window changes size
  * Use the current client tmux session when splitting a new client
  * python.kak: restore cleaning up trailing whitespaces on newline
  * static_words def style tweak in c-family.kak
  * Restore whitespace cleanup on InsertEnd in python.kak
* Mon May  2 2016 mpluskal@suse.com
- Update to version 0.0+git.20160430:
  * Fix comparison operators in utf8_iterator and tag it as bidirectional
  * Add checked, explicit conversion from strongly typed number for size_t
  * Make use of strongly typed number to size_t conversion
  * Add missing include in file.cc
  * Add another missing include in shell_manager.cc
  * Fix test runner use of sed -r
  * Fix handling of expected to fail tests
  * Fix wrap_lines
  * Check all buffer are saved in :kill, and add :kill! to avoid that
  * Fix splitting selecting the first buffer char when there is a match at buffer begin
- Update _service
* Wed Apr 27 2016 mvetter@suse.com
- Update to latest git
* Fri Nov 13 2015 mvetter@suse.com
- Use optflags
* Fri Nov 13 2015 mvetter@suse.com
- Disable autorun of service
- Set proper version
* Thu Nov 12 2015 mvetter@suse.com
- Set PREFIX to use /usr instead of /usr/local
* Tue Nov 10 2015 mvetter@suse.com
- Creating initial package for openSUSE
  So far kakoune isnt versioned thus creating git package.

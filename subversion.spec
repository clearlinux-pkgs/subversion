#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : subversion
Version  : 1.14.2
Release  : 35
URL      : https://apache.osuosl.org/subversion/subversion-1.14.2.tar.gz
Source0  : https://apache.osuosl.org/subversion/subversion-1.14.2.tar.gz
Summary  : Subversion SVN Protocol Repository Access Library
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause MIT
Requires: subversion-bin = %{version}-%{release}
Requires: subversion-lib = %{version}-%{release}
Requires: subversion-license = %{version}-%{release}
Requires: subversion-locales = %{version}-%{release}
Requires: subversion-man = %{version}-%{release}
Requires: subversion-perl = %{version}-%{release}
BuildRequires : apr-dev
BuildRequires : apr-util-dev
BuildRequires : buildreq-distutils3
BuildRequires : cyrus-sasl-dev
BuildRequires : dbus-dev
BuildRequires : doxygen
BuildRequires : expat-dev
BuildRequires : file-dev
BuildRequires : libsecret-dev
BuildRequires : pkgconfig(liblz4)
BuildRequires : pkgconfig(serf-1)
BuildRequires : pkgconfig(zlib)
BuildRequires : python3
BuildRequires : ruby
BuildRequires : sed
BuildRequires : serf-dev
BuildRequires : sqlite-autoconf-dev
Patch1: 0001-test-skip-tests-that-are-not-python3-ready.patch

%description
Subversion, a version control system.
=====================================
$LastChangedDate: 2022-03-31 13:42:28 +0000 (Thu, 31 Mar 2022) $

%package bin
Summary: bin components for the subversion package.
Group: Binaries
Requires: subversion-license = %{version}-%{release}

%description bin
bin components for the subversion package.


%package dev
Summary: dev components for the subversion package.
Group: Development
Requires: subversion-lib = %{version}-%{release}
Requires: subversion-bin = %{version}-%{release}
Provides: subversion-devel = %{version}-%{release}
Requires: subversion = %{version}-%{release}

%description dev
dev components for the subversion package.


%package lib
Summary: lib components for the subversion package.
Group: Libraries
Requires: subversion-license = %{version}-%{release}

%description lib
lib components for the subversion package.


%package license
Summary: license components for the subversion package.
Group: Default

%description license
license components for the subversion package.


%package locales
Summary: locales components for the subversion package.
Group: Default

%description locales
locales components for the subversion package.


%package man
Summary: man components for the subversion package.
Group: Default

%description man
man components for the subversion package.


%package perl
Summary: perl components for the subversion package.
Group: Default
Requires: subversion = %{version}-%{release}

%description perl
perl components for the subversion package.


%prep
%setup -q -n subversion-1.14.2
cd %{_builddir}/subversion-1.14.2
%patch1 -p1

%build
## build_prepend content
export CPPFLAGS=-P
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664905942
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --with-utf8proc=internal \
--without-swig \
--with-serf \
--with-gnome-keyring
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check PARALLEL=1 || :

%install
export SOURCE_DATE_EPOCH=1664905942
rm -rf %{buildroot}
## install_prepend content
make swig-pl DESTDIR=%{buildroot}
## install_prepend end
mkdir -p %{buildroot}/usr/share/package-licenses/subversion
cp %{_builddir}/subversion-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/subversion/2001ec12a76fab136661bf0850b354ce06312809 || :
cp %{_builddir}/subversion-%{version}/subversion/libsvn_subr/lz4/LICENSE %{buildroot}/usr/share/package-licenses/subversion/10bf56381baaf07f0647b93a810eb4e7e9545e8d || :
cp %{_builddir}/subversion-%{version}/subversion/libsvn_subr/utf8proc/LICENSE.md %{buildroot}/usr/share/package-licenses/subversion/1383cee8b844e0df97aea12a3ea98912af5081dd || :
cp %{_builddir}/subversion-%{version}/tools/dev/svnmover/linenoise/LICENSE %{buildroot}/usr/share/package-licenses/subversion/3bd655bcdbe6f4f14e9da385f1953c50dd89ea8e || :
%make_install
%find_lang subversion
## install_append content
make install-swig-pl DESTDIR=%{buildroot} LIBRARY_PATH=%{buildroot}/usr/lib64 INSTALLDIRS=vendor

# Clean up unwanted files.  These are usually handled as part of install step,
# before we are able to install the bindings above.
rm -f %{buildroot}/usr/lib/perl5/*/*/perllocal.pod
rm -f %{buildroot}/usr/lib64/*.la
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/svn
/usr/bin/svnadmin
/usr/bin/svnbench
/usr/bin/svndumpfilter
/usr/bin/svnfsfs
/usr/bin/svnlook
/usr/bin/svnmucc
/usr/bin/svnrdump
/usr/bin/svnserve
/usr/bin/svnsync
/usr/bin/svnversion

%files dev
%defattr(-,root,root,-)
/usr/include/subversion-1/mod_authz_svn.h
/usr/include/subversion-1/mod_dav_svn.h
/usr/include/subversion-1/svn-revision.txt
/usr/include/subversion-1/svn_auth.h
/usr/include/subversion-1/svn_base64.h
/usr/include/subversion-1/svn_cache_config.h
/usr/include/subversion-1/svn_checksum.h
/usr/include/subversion-1/svn_client.h
/usr/include/subversion-1/svn_cmdline.h
/usr/include/subversion-1/svn_compat.h
/usr/include/subversion-1/svn_config.h
/usr/include/subversion-1/svn_ctype.h
/usr/include/subversion-1/svn_dav.h
/usr/include/subversion-1/svn_delta.h
/usr/include/subversion-1/svn_diff.h
/usr/include/subversion-1/svn_dirent_uri.h
/usr/include/subversion-1/svn_dso.h
/usr/include/subversion-1/svn_error.h
/usr/include/subversion-1/svn_error_codes.h
/usr/include/subversion-1/svn_fs.h
/usr/include/subversion-1/svn_hash.h
/usr/include/subversion-1/svn_io.h
/usr/include/subversion-1/svn_iter.h
/usr/include/subversion-1/svn_md5.h
/usr/include/subversion-1/svn_mergeinfo.h
/usr/include/subversion-1/svn_nls.h
/usr/include/subversion-1/svn_opt.h
/usr/include/subversion-1/svn_opt_impl.h
/usr/include/subversion-1/svn_path.h
/usr/include/subversion-1/svn_pools.h
/usr/include/subversion-1/svn_props.h
/usr/include/subversion-1/svn_quoprint.h
/usr/include/subversion-1/svn_ra.h
/usr/include/subversion-1/svn_ra_svn.h
/usr/include/subversion-1/svn_repos.h
/usr/include/subversion-1/svn_sorts.h
/usr/include/subversion-1/svn_string.h
/usr/include/subversion-1/svn_subst.h
/usr/include/subversion-1/svn_time.h
/usr/include/subversion-1/svn_types.h
/usr/include/subversion-1/svn_types_impl.h
/usr/include/subversion-1/svn_user.h
/usr/include/subversion-1/svn_utf.h
/usr/include/subversion-1/svn_version.h
/usr/include/subversion-1/svn_wc.h
/usr/include/subversion-1/svn_x509.h
/usr/include/subversion-1/svn_xml.h
/usr/lib64/libsvn_auth_gnome_keyring-1.so
/usr/lib64/libsvn_client-1.so
/usr/lib64/libsvn_delta-1.so
/usr/lib64/libsvn_diff-1.so
/usr/lib64/libsvn_fs-1.so
/usr/lib64/libsvn_fs_fs-1.so
/usr/lib64/libsvn_fs_util-1.so
/usr/lib64/libsvn_fs_x-1.so
/usr/lib64/libsvn_ra-1.so
/usr/lib64/libsvn_ra_local-1.so
/usr/lib64/libsvn_ra_serf-1.so
/usr/lib64/libsvn_ra_svn-1.so
/usr/lib64/libsvn_repos-1.so
/usr/lib64/libsvn_subr-1.so
/usr/lib64/libsvn_swig_perl-1.so
/usr/lib64/libsvn_wc-1.so
/usr/lib64/pkgconfig/libsvn_auth_gnome_keyring.pc
/usr/lib64/pkgconfig/libsvn_client.pc
/usr/lib64/pkgconfig/libsvn_delta.pc
/usr/lib64/pkgconfig/libsvn_diff.pc
/usr/lib64/pkgconfig/libsvn_fs.pc
/usr/lib64/pkgconfig/libsvn_fs_fs.pc
/usr/lib64/pkgconfig/libsvn_fs_util.pc
/usr/lib64/pkgconfig/libsvn_fs_x.pc
/usr/lib64/pkgconfig/libsvn_ra.pc
/usr/lib64/pkgconfig/libsvn_ra_local.pc
/usr/lib64/pkgconfig/libsvn_ra_serf.pc
/usr/lib64/pkgconfig/libsvn_ra_svn.pc
/usr/lib64/pkgconfig/libsvn_repos.pc
/usr/lib64/pkgconfig/libsvn_subr.pc
/usr/lib64/pkgconfig/libsvn_wc.pc
/usr/share/man/man3/SVN::Base.3
/usr/share/man/man3/SVN::Client.3
/usr/share/man/man3/SVN::Core.3
/usr/share/man/man3/SVN::Delta.3
/usr/share/man/man3/SVN::Fs.3
/usr/share/man/man3/SVN::Ra.3
/usr/share/man/man3/SVN::Repos.3
/usr/share/man/man3/SVN::Wc.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/libsvn_auth_gnome_keyring-1.so.0
/usr/lib64/libsvn_auth_gnome_keyring-1.so.0.0.0
/usr/lib64/libsvn_client-1.so.0
/usr/lib64/libsvn_client-1.so.0.0.0
/usr/lib64/libsvn_delta-1.so.0
/usr/lib64/libsvn_delta-1.so.0.0.0
/usr/lib64/libsvn_diff-1.so.0
/usr/lib64/libsvn_diff-1.so.0.0.0
/usr/lib64/libsvn_fs-1.so.0
/usr/lib64/libsvn_fs-1.so.0.0.0
/usr/lib64/libsvn_fs_fs-1.so.0
/usr/lib64/libsvn_fs_fs-1.so.0.0.0
/usr/lib64/libsvn_fs_util-1.so.0
/usr/lib64/libsvn_fs_util-1.so.0.0.0
/usr/lib64/libsvn_fs_x-1.so.0
/usr/lib64/libsvn_fs_x-1.so.0.0.0
/usr/lib64/libsvn_ra-1.so.0
/usr/lib64/libsvn_ra-1.so.0.0.0
/usr/lib64/libsvn_ra_local-1.so.0
/usr/lib64/libsvn_ra_local-1.so.0.0.0
/usr/lib64/libsvn_ra_serf-1.so.0
/usr/lib64/libsvn_ra_serf-1.so.0.0.0
/usr/lib64/libsvn_ra_svn-1.so.0
/usr/lib64/libsvn_ra_svn-1.so.0.0.0
/usr/lib64/libsvn_repos-1.so.0
/usr/lib64/libsvn_repos-1.so.0.0.0
/usr/lib64/libsvn_subr-1.so.0
/usr/lib64/libsvn_subr-1.so.0.0.0
/usr/lib64/libsvn_swig_perl-1.so.0
/usr/lib64/libsvn_swig_perl-1.so.0.0.0
/usr/lib64/libsvn_wc-1.so.0
/usr/lib64/libsvn_wc-1.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/subversion/10bf56381baaf07f0647b93a810eb4e7e9545e8d
/usr/share/package-licenses/subversion/1383cee8b844e0df97aea12a3ea98912af5081dd
/usr/share/package-licenses/subversion/2001ec12a76fab136661bf0850b354ce06312809
/usr/share/package-licenses/subversion/3bd655bcdbe6f4f14e9da385f1953c50dd89ea8e

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/svn.1
/usr/share/man/man1/svnadmin.1
/usr/share/man/man1/svndumpfilter.1
/usr/share/man/man1/svnlook.1
/usr/share/man/man1/svnmucc.1
/usr/share/man/man1/svnrdump.1
/usr/share/man/man1/svnsync.1
/usr/share/man/man1/svnversion.1
/usr/share/man/man5/svnserve.conf.5
/usr/share/man/man8/svnserve.8

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*

%files locales -f subversion.lang
%defattr(-,root,root,-)


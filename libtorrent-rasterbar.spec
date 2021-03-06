#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libtorrent-rasterbar
Version  : 1.2.10
Release  : 9
URL      : file:///insilications/build/clearlinux/packages/libtorrent-rasterbar/libtorrent-rasterbar-libtorrent-1.2.10.tar.gz
Source0  : file:///insilications/build/clearlinux/packages/libtorrent-rasterbar/libtorrent-rasterbar-libtorrent-1.2.10.tar.gz
Summary  : Bittorrent library.
Group    : Development/Tools
License  : BSD-2-Clause
Requires: libtorrent-rasterbar-data = %{version}-%{release}
Requires: libtorrent-rasterbar-lib = %{version}-%{release}
BuildRequires : boost-dev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-configure
BuildRequires : buildreq-distutils3
BuildRequires : openssl-dev
BuildRequires : openssl-staticdev
BuildRequires : pkgconfig(libcrypto)
BuildRequires : pkgconfig(libssl)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(zlib)
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
libtorrent
----------
.. image:: https://travis-ci.org/arvidn/libtorrent.svg?branch=master
:target: https://travis-ci.org/arvidn/libtorrent

%package data
Summary: data components for the libtorrent-rasterbar package.
Group: Data

%description data
data components for the libtorrent-rasterbar package.


%package dev
Summary: dev components for the libtorrent-rasterbar package.
Group: Development
Requires: libtorrent-rasterbar-lib = %{version}-%{release}
Requires: libtorrent-rasterbar-data = %{version}-%{release}
Provides: libtorrent-rasterbar-devel = %{version}-%{release}
Requires: libtorrent-rasterbar = %{version}-%{release}

%description dev
dev components for the libtorrent-rasterbar package.


%package lib
Summary: lib components for the libtorrent-rasterbar package.
Group: Libraries
Requires: libtorrent-rasterbar-data = %{version}-%{release}

%description lib
lib components for the libtorrent-rasterbar package.


%package staticdev
Summary: staticdev components for the libtorrent-rasterbar package.
Group: Default
Requires: libtorrent-rasterbar-dev = %{version}-%{release}

%description staticdev
staticdev components for the libtorrent-rasterbar package.


%prep
%setup -q -n libtorrent-rasterbar
cd %{_builddir}/libtorrent-rasterbar

%build
## build_prepend content
./autotool.sh
## build_prepend end
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1601594253
export GCC_IGNORE_WERROR=1
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -std=c++14 -ffat-lto-objects -fPIC $PGO_GEN"
export FCFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -std=c++14 -ffat-lto-objects -fPIC $PGO_GEN"
export FFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -std=c++14 -ffat-lto-objects -fPIC $PGO_GEN"
export CXXFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe -std=c++14 -ffat-lto-objects -fPIC $PGO_GEN"
export LDFLAGS_GENERATE="-O3 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -std=c++14 -ffat-lto-objects -fPIC $PGO_GEN"
## pgo use
## -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden -flto-partition=none
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -std=c++14 -ffat-lto-objects -fPIC $PGO_USE"
export FCFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -std=c++14 -ffat-lto-objects -fPIC $PGO_USE"
export FFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -std=c++14 -ffat-lto-objects -fPIC $PGO_USE"
export CXXFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -std=c++14 -ffat-lto-objects -fPIC $PGO_USE"
export LDFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -std=c++14 -ffat-lto-objects -fPIC $PGO_USE"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%define _lto_cflags 1
#%define _lto_cflags %{nil}
#
# export PATH="/usr/lib64/ccache/bin:$PATH"
# export CCACHE_NOHASHDIR=1
# export CCACHE_DIRECT=1
# export CCACHE_SLOPPINESS=pch_defines,locale,time_macros
# export CCACHE_DISABLE=1
# LDFLAGS="${LDFLAGS} -Wl,--whole-archive /usr/lib64/libz.a /usr/lib64/libssl.a /usr/lib64/libcrypto.a /usr/lib64/libz.a -pthread -ldl -lm -lmvec -Wl,--no-whole-archive"
## altflags_pgo end
##
%define _lto_cflags 1
##
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
 %configure --enable-shared --enable-static --enable-dht --enable-encryption --enable-tests --disable-python-binding
make  %{?_smp_mflags}

make check || :
make clean
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
%configure --enable-shared --enable-static --enable-dht --enable-encryption --enable-tests --disable-python-binding
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1601594253
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/cmake/*

%files dev
%defattr(-,root,root,-)
/usr/include/libtorrent/add_torrent_params.hpp
/usr/include/libtorrent/address.hpp
/usr/include/libtorrent/alert.hpp
/usr/include/libtorrent/alert_manager.hpp
/usr/include/libtorrent/alert_types.hpp
/usr/include/libtorrent/announce_entry.hpp
/usr/include/libtorrent/assert.hpp
/usr/include/libtorrent/aux_/aligned_storage.hpp
/usr/include/libtorrent/aux_/aligned_union.hpp
/usr/include/libtorrent/aux_/alloca.hpp
/usr/include/libtorrent/aux_/allocating_handler.hpp
/usr/include/libtorrent/aux_/array.hpp
/usr/include/libtorrent/aux_/bind_to_device.hpp
/usr/include/libtorrent/aux_/block_cache_reference.hpp
/usr/include/libtorrent/aux_/byteswap.hpp
/usr/include/libtorrent/aux_/container_wrapper.hpp
/usr/include/libtorrent/aux_/cppint_import_export.hpp
/usr/include/libtorrent/aux_/cpuid.hpp
/usr/include/libtorrent/aux_/deferred_handler.hpp
/usr/include/libtorrent/aux_/deprecated.hpp
/usr/include/libtorrent/aux_/deque.hpp
/usr/include/libtorrent/aux_/dev_random.hpp
/usr/include/libtorrent/aux_/disable_warnings_pop.hpp
/usr/include/libtorrent/aux_/disable_warnings_push.hpp
/usr/include/libtorrent/aux_/disk_job_fence.hpp
/usr/include/libtorrent/aux_/escape_string.hpp
/usr/include/libtorrent/aux_/export.hpp
/usr/include/libtorrent/aux_/ffs.hpp
/usr/include/libtorrent/aux_/file_progress.hpp
/usr/include/libtorrent/aux_/generate_peer_id.hpp
/usr/include/libtorrent/aux_/has_block.hpp
/usr/include/libtorrent/aux_/instantiate_connection.hpp
/usr/include/libtorrent/aux_/io.hpp
/usr/include/libtorrent/aux_/ip_notifier.hpp
/usr/include/libtorrent/aux_/keepalive.hpp
/usr/include/libtorrent/aux_/listen_socket_handle.hpp
/usr/include/libtorrent/aux_/lsd.hpp
/usr/include/libtorrent/aux_/merkle.hpp
/usr/include/libtorrent/aux_/noexcept_movable.hpp
/usr/include/libtorrent/aux_/numeric_cast.hpp
/usr/include/libtorrent/aux_/openssl.hpp
/usr/include/libtorrent/aux_/path.hpp
/usr/include/libtorrent/aux_/portmap.hpp
/usr/include/libtorrent/aux_/proxy_settings.hpp
/usr/include/libtorrent/aux_/range.hpp
/usr/include/libtorrent/aux_/route.h
/usr/include/libtorrent/aux_/scope_end.hpp
/usr/include/libtorrent/aux_/session_call.hpp
/usr/include/libtorrent/aux_/session_impl.hpp
/usr/include/libtorrent/aux_/session_interface.hpp
/usr/include/libtorrent/aux_/session_settings.hpp
/usr/include/libtorrent/aux_/session_udp_sockets.hpp
/usr/include/libtorrent/aux_/set_socket_buffer.hpp
/usr/include/libtorrent/aux_/socket_type.hpp
/usr/include/libtorrent/aux_/storage_piece_set.hpp
/usr/include/libtorrent/aux_/storage_utils.hpp
/usr/include/libtorrent/aux_/string_ptr.hpp
/usr/include/libtorrent/aux_/suggest_piece.hpp
/usr/include/libtorrent/aux_/throw.hpp
/usr/include/libtorrent/aux_/time.hpp
/usr/include/libtorrent/aux_/torrent_impl.hpp
/usr/include/libtorrent/aux_/unique_ptr.hpp
/usr/include/libtorrent/aux_/vector.hpp
/usr/include/libtorrent/aux_/win_crypto_provider.hpp
/usr/include/libtorrent/aux_/win_util.hpp
/usr/include/libtorrent/aux_/windows.hpp
/usr/include/libtorrent/bandwidth_limit.hpp
/usr/include/libtorrent/bandwidth_manager.hpp
/usr/include/libtorrent/bandwidth_queue_entry.hpp
/usr/include/libtorrent/bandwidth_socket.hpp
/usr/include/libtorrent/bdecode.hpp
/usr/include/libtorrent/bencode.hpp
/usr/include/libtorrent/bitfield.hpp
/usr/include/libtorrent/block_cache.hpp
/usr/include/libtorrent/bloom_filter.hpp
/usr/include/libtorrent/broadcast_socket.hpp
/usr/include/libtorrent/bt_peer_connection.hpp
/usr/include/libtorrent/buffer.hpp
/usr/include/libtorrent/chained_buffer.hpp
/usr/include/libtorrent/choker.hpp
/usr/include/libtorrent/close_reason.hpp
/usr/include/libtorrent/config.hpp
/usr/include/libtorrent/copy_ptr.hpp
/usr/include/libtorrent/crc32c.hpp
/usr/include/libtorrent/create_torrent.hpp
/usr/include/libtorrent/deadline_timer.hpp
/usr/include/libtorrent/debug.hpp
/usr/include/libtorrent/disk_buffer_holder.hpp
/usr/include/libtorrent/disk_buffer_pool.hpp
/usr/include/libtorrent/disk_interface.hpp
/usr/include/libtorrent/disk_io_job.hpp
/usr/include/libtorrent/disk_io_thread.hpp
/usr/include/libtorrent/disk_io_thread_pool.hpp
/usr/include/libtorrent/disk_job_pool.hpp
/usr/include/libtorrent/disk_observer.hpp
/usr/include/libtorrent/download_priority.hpp
/usr/include/libtorrent/ed25519.hpp
/usr/include/libtorrent/entry.hpp
/usr/include/libtorrent/enum_net.hpp
/usr/include/libtorrent/error.hpp
/usr/include/libtorrent/error_code.hpp
/usr/include/libtorrent/extensions.hpp
/usr/include/libtorrent/extensions/smart_ban.hpp
/usr/include/libtorrent/extensions/ut_metadata.hpp
/usr/include/libtorrent/extensions/ut_pex.hpp
/usr/include/libtorrent/file.hpp
/usr/include/libtorrent/file_pool.hpp
/usr/include/libtorrent/file_storage.hpp
/usr/include/libtorrent/fingerprint.hpp
/usr/include/libtorrent/flags.hpp
/usr/include/libtorrent/fwd.hpp
/usr/include/libtorrent/gzip.hpp
/usr/include/libtorrent/hasher.hpp
/usr/include/libtorrent/hasher512.hpp
/usr/include/libtorrent/heterogeneous_queue.hpp
/usr/include/libtorrent/hex.hpp
/usr/include/libtorrent/http_connection.hpp
/usr/include/libtorrent/http_parser.hpp
/usr/include/libtorrent/http_seed_connection.hpp
/usr/include/libtorrent/http_stream.hpp
/usr/include/libtorrent/http_tracker_connection.hpp
/usr/include/libtorrent/i2p_stream.hpp
/usr/include/libtorrent/identify_client.hpp
/usr/include/libtorrent/index_range.hpp
/usr/include/libtorrent/invariant_check.hpp
/usr/include/libtorrent/io.hpp
/usr/include/libtorrent/io_service.hpp
/usr/include/libtorrent/io_service_fwd.hpp
/usr/include/libtorrent/ip_filter.hpp
/usr/include/libtorrent/ip_voter.hpp
/usr/include/libtorrent/kademlia/announce_flags.hpp
/usr/include/libtorrent/kademlia/dht_observer.hpp
/usr/include/libtorrent/kademlia/dht_settings.hpp
/usr/include/libtorrent/kademlia/dht_state.hpp
/usr/include/libtorrent/kademlia/dht_storage.hpp
/usr/include/libtorrent/kademlia/dht_tracker.hpp
/usr/include/libtorrent/kademlia/direct_request.hpp
/usr/include/libtorrent/kademlia/dos_blocker.hpp
/usr/include/libtorrent/kademlia/ed25519.hpp
/usr/include/libtorrent/kademlia/find_data.hpp
/usr/include/libtorrent/kademlia/get_item.hpp
/usr/include/libtorrent/kademlia/get_peers.hpp
/usr/include/libtorrent/kademlia/io.hpp
/usr/include/libtorrent/kademlia/item.hpp
/usr/include/libtorrent/kademlia/msg.hpp
/usr/include/libtorrent/kademlia/node.hpp
/usr/include/libtorrent/kademlia/node_entry.hpp
/usr/include/libtorrent/kademlia/node_id.hpp
/usr/include/libtorrent/kademlia/observer.hpp
/usr/include/libtorrent/kademlia/put_data.hpp
/usr/include/libtorrent/kademlia/refresh.hpp
/usr/include/libtorrent/kademlia/routing_table.hpp
/usr/include/libtorrent/kademlia/rpc_manager.hpp
/usr/include/libtorrent/kademlia/sample_infohashes.hpp
/usr/include/libtorrent/kademlia/traversal_algorithm.hpp
/usr/include/libtorrent/kademlia/types.hpp
/usr/include/libtorrent/lazy_entry.hpp
/usr/include/libtorrent/link.hpp
/usr/include/libtorrent/linked_list.hpp
/usr/include/libtorrent/lsd.hpp
/usr/include/libtorrent/magnet_uri.hpp
/usr/include/libtorrent/natpmp.hpp
/usr/include/libtorrent/netlink.hpp
/usr/include/libtorrent/operations.hpp
/usr/include/libtorrent/optional.hpp
/usr/include/libtorrent/packet_buffer.hpp
/usr/include/libtorrent/packet_pool.hpp
/usr/include/libtorrent/parse_url.hpp
/usr/include/libtorrent/part_file.hpp
/usr/include/libtorrent/pe_crypto.hpp
/usr/include/libtorrent/peer.hpp
/usr/include/libtorrent/peer_class.hpp
/usr/include/libtorrent/peer_class_set.hpp
/usr/include/libtorrent/peer_class_type_filter.hpp
/usr/include/libtorrent/peer_connection.hpp
/usr/include/libtorrent/peer_connection_handle.hpp
/usr/include/libtorrent/peer_connection_interface.hpp
/usr/include/libtorrent/peer_id.hpp
/usr/include/libtorrent/peer_info.hpp
/usr/include/libtorrent/peer_list.hpp
/usr/include/libtorrent/peer_request.hpp
/usr/include/libtorrent/performance_counters.hpp
/usr/include/libtorrent/pex_flags.hpp
/usr/include/libtorrent/piece_block.hpp
/usr/include/libtorrent/piece_block_progress.hpp
/usr/include/libtorrent/piece_picker.hpp
/usr/include/libtorrent/platform_util.hpp
/usr/include/libtorrent/portmap.hpp
/usr/include/libtorrent/proxy_base.hpp
/usr/include/libtorrent/puff.hpp
/usr/include/libtorrent/random.hpp
/usr/include/libtorrent/read_resume_data.hpp
/usr/include/libtorrent/receive_buffer.hpp
/usr/include/libtorrent/request_blocks.hpp
/usr/include/libtorrent/resolve_links.hpp
/usr/include/libtorrent/resolver.hpp
/usr/include/libtorrent/resolver_interface.hpp
/usr/include/libtorrent/session.hpp
/usr/include/libtorrent/session_handle.hpp
/usr/include/libtorrent/session_settings.hpp
/usr/include/libtorrent/session_stats.hpp
/usr/include/libtorrent/session_status.hpp
/usr/include/libtorrent/session_types.hpp
/usr/include/libtorrent/settings_pack.hpp
/usr/include/libtorrent/sha1.hpp
/usr/include/libtorrent/sha1_hash.hpp
/usr/include/libtorrent/sha512.hpp
/usr/include/libtorrent/sliding_average.hpp
/usr/include/libtorrent/socket.hpp
/usr/include/libtorrent/socket_io.hpp
/usr/include/libtorrent/socks5_stream.hpp
/usr/include/libtorrent/span.hpp
/usr/include/libtorrent/ssl_stream.hpp
/usr/include/libtorrent/stack_allocator.hpp
/usr/include/libtorrent/stat.hpp
/usr/include/libtorrent/stat_cache.hpp
/usr/include/libtorrent/storage.hpp
/usr/include/libtorrent/storage_defs.hpp
/usr/include/libtorrent/string_util.hpp
/usr/include/libtorrent/string_view.hpp
/usr/include/libtorrent/tailqueue.hpp
/usr/include/libtorrent/time.hpp
/usr/include/libtorrent/timestamp_history.hpp
/usr/include/libtorrent/torrent.hpp
/usr/include/libtorrent/torrent_flags.hpp
/usr/include/libtorrent/torrent_handle.hpp
/usr/include/libtorrent/torrent_info.hpp
/usr/include/libtorrent/torrent_peer.hpp
/usr/include/libtorrent/torrent_peer_allocator.hpp
/usr/include/libtorrent/torrent_status.hpp
/usr/include/libtorrent/tracker_manager.hpp
/usr/include/libtorrent/udp_socket.hpp
/usr/include/libtorrent/udp_tracker_connection.hpp
/usr/include/libtorrent/union_endpoint.hpp
/usr/include/libtorrent/units.hpp
/usr/include/libtorrent/upnp.hpp
/usr/include/libtorrent/utf8.hpp
/usr/include/libtorrent/utp_socket_manager.hpp
/usr/include/libtorrent/utp_stream.hpp
/usr/include/libtorrent/vector_utils.hpp
/usr/include/libtorrent/version.hpp
/usr/include/libtorrent/web_connection_base.hpp
/usr/include/libtorrent/web_peer_connection.hpp
/usr/include/libtorrent/write_resume_data.hpp
/usr/include/libtorrent/xml_parse.hpp
/usr/lib64/libtorrent-rasterbar.so
/usr/lib64/pkgconfig/libtorrent-rasterbar.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libtorrent-rasterbar.so.10
/usr/lib64/libtorrent-rasterbar.so.10.0.0

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libtorrent-rasterbar.a
